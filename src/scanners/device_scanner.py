from src.network.net_device import NetDevice
from config.settings import get_device_credentials
from datetime import datetime
from src.parsers.cisco_ios_parser import parse_show_version

class DeviceScanner:
    def scan_device(self, device):
        username, password = get_device_credentials(device)

        target = NetDevice(device.mgmt_ip, username, password, device.os_type)

        status = target.connect()
        if status:
            version_output = target.send_command("show version")
            inventory_output = target.send_command("show inventory")
            parsed_version_output = parse_show_version(version_output)
            target.disconnect()
            scan_time = datetime.now()
            device.last_scanned = scan_time.isoformat()
            if parsed_version_output is not None:
                device.scan_status = "success"
                device.model = parsed_version_output["MODEL"]
                device.serial_number = parsed_version_output["SERIAL_NUMBER"]
                device.collected_os_version = parsed_version_output["OS_VERSION"]
                device.uptime = parsed_version_output["UPTIME"]
            if parsed_version_output is None:
                device.scan_status = "partial"
            return {
                'success': True,
                'version': parsed_version_output,
                'inventory': inventory_output
            }
        else:
            print(f"Can't connect to device {device.hostname}")
            scan_time = datetime.now()
            device.last_scanned = scan_time.isoformat()
            device.scan_status = "failed"
            return {
                'success': False,
                'status': target.status,
                'error': target.error
            }

    def scan_all_devices(self, devices):
        outputs = []
        for each in devices:
            output = self.scan_device(each)
            if output['success']:
                outputs.append({"device": each, "output": output})
            else:
                print(f"Skipping device {each.hostname}")
                outputs.append({"device": each, "output": output})
        return outputs

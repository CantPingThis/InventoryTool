from src.network.net_device import NetDevice
from config.settings import get_device_credentials

class DeviceScanner:
    def scan_device(self, device):
        username, password = get_device_credentials(device)

        target = NetDevice(device.mgmt_ip, username, password, device.os_type)

        status = target.connect()
        if status:
            version_output = target.send_command("show version")
            inventory_output = target.send_command("show inventory")
            target.disconnect()
            return {
                'success': True,
                'version': version_output,
                'inventory': inventory_output
            }
        else:
            print(f"Can't connect to device {device.hostname}")
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

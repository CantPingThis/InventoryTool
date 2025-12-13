from src.models.device import Device
from src.storage.file_storage import save_inventory_to_json
from config.settings import load_yaml_inventory, get_device_credentials

class InventoryManager:
    def __init__(self):
        self.devices = []
    
    def load_from_yaml(self):
        raw_devices = load_yaml_inventory()
        self.devices = self._convert_to_devices(raw_devices)
        return self.devices
    
    def _convert_to_devices(self, raw_devices):
        devices = []
        for each in raw_devices:
            usern, passw = get_device_credentials(each)
            device = Device(
                hostname=each.get("hostname").strip(),
                mgmt_ip=each.get("mgmt_ip").strip(),
                site=each.get("site").strip(),
                role=each.get("role").strip(),
                vendor=each.get("vendor") or None,
                os_type=each.get("os_type") or None,
                os_version=each.get("os_version") or None
            )
            devices.append(device)
        return devices
    
    def get_device_count(self):
        return len(self.devices)
    
    def display_inventory(self):
        print(f"\nFound {self.get_device_count()} devices:\n")
        for device in self.devices:
            print(device)
    
    def save_to_json(self):
        save_inventory_to_json(self.devices, self.get_device_count())
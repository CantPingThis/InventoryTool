import yaml
from pathlib import Path

yaml_inventory = "config/devices.yaml"

path = Path(yaml_inventory)

def list_from_yaml():
    if not path.exists():
        print("File does not exist")
    with open(path, "r") as f:
        raw_data = yaml.safe_load(f)
        devices = raw_data.get("devices")
        list_devices = []
        for each in devices:
            list_devices.append(
                dict(
                    hostname=each.get("hostname").strip(),
                    mgmt_ip=each.get("mgmt_ip").strip(),
                    site=each.get("site").strip(),
                    role=each.get("role").strip(),
                    vendor=each.get("vendor") or "",
                    os_type=each.get("os_type") or "",
                    os_version=each.get("os_version") or ""
                )
            )
        return list_devices
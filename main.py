import argparse
from src.collectors.inventory_manager import InventoryManager
from src.scanners.device_scanner import DeviceScanner

def main():
    manager = InventoryManager()
    manager.load_from_yaml()
    manager.display_inventory()
    
    scanner = DeviceScanner()
    scan_results = scanner.scan_all_devices(manager.devices)
    success_device = []
    print(scan_results)
    for result in scan_results:
        device = result['device']
        output = result['output']
        if output.get('success') == True:
            success_device.append(device.hostname)
            print(f"\nScanned {device.hostname}:")
            print(f"    Version output: {output['version']}")
            print(f"    Inventory output: {len(output['inventory'])} characters")
        else:
            print(f"Failed to scan device {device.hostname}: {output.get('error', 'Unknown error')}")
    
    print("\nScan results:")
    print(f"Success on : {len(success_device)} devices")
    print(f"Failed on : {len(scan_results) - len(success_device)} devices")

    manager.save_to_json()
    
if __name__ == "__main__":
    main()
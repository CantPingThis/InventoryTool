import argparse
from src.collectors.inventory_manager import InventoryManager

def main():
    manager = InventoryManager()
    manager.load_from_yaml()
    manager.display_inventory()
    manager.save_to_json()
    
if __name__ == "__main__":
    main()
from src.collectors.inventory_manager import InventoryManager

def test_inventory_manager_load_from_yaml():
    # Arrange
    manager = InventoryManager()

    # Act
    manager.load_from_yaml("tests/test_devices.yaml")

    # Assert
    assert len(manager.devices) == 1
    assert manager.devices[0].hostname == "TEST-SW-001"
    assert manager.devices[0].mgmt_ip == "192.168.1.1"
    assert manager.devices[0].site == "TEST-LAB"
    assert manager.devices[0].role == "access"
    assert manager.devices[0].os_type == "cisco_ios"
    assert manager.devices[0].vendor == "Cisco"
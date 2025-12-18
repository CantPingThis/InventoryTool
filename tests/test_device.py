from src.models.device import Device

def test_device_creation():
    test_device = Device(
        hostname = "TEST_SW",
        mgmt_ip = "10.0.0.1",
        site = "LAB",
        role = "access",
        os_type = "cisco_ios"
    )
    assert test_device.hostname == "TEST_SW"
    assert test_device.mgmt_ip == "10.0.0.1"
    assert test_device.site == "LAB"
    assert test_device.role == "access"
    assert test_device.os_type == "cisco_ios"
    assert test_device.vendor is None
    assert test_device.os_version is None
    assert test_device.model is None
    assert test_device.serial_number is None
    assert test_device.collected_os_version is None
    assert test_device.uptime is None
    assert test_device.last_scanned is None
    assert test_device.scan_status is None

def test_device_str_method():
    # Test 1: Never scanned device (scan_status = None)
    test_device = Device(
        hostname="TEST_SW",
        mgmt_ip="10.0.0.1",
        site="LAB",
        role="access",
        os_type="cisco_ios"
    )

    result = str(test_device)
    assert "Never scanned device" in result
    assert "TEST_SW" in result

    # Test 2 : Successfully scanned device
    test_device.scan_status = "success"
    test_device.last_scanned = "2025-12-18T10:30:00"
    test_device.model = "C9200-24P"
    test_device.serial_number = "ABC123"
    test_device.collected_os_version = "17.3.1"
    test_device.uptime = "5 days, 2 hours"

    result = str(test_device)
    assert "Last scan status : Success" in result
    assert "Model: C9200-24P" in result
    assert "Serial Number: ABC123" in result

    test_device2 = Device(
        hostname="FAIL_SW",
        mgmt_ip="10.0.0.2",
        site="LAB",
        role="access",
        os_type="cisco_ios"
    )

    test_device2.scan_status = "failed"
    test_device2.last_scanned = "2025-12-18T10:35:00"

    result = str(test_device2)
    assert "Last scan status : Failed" in result

def test_device_to_dict():
    test_device = Device(
        hostname = "TEST_SW",
        mgmt_ip = "10.0.0.1",
        site = "LAB",
        role = "access",
        os_type = "cisco_ios"
    )

    # Act
    result = test_device.to_dict()

    # Assert
    assert result == {
        'hostname': 'TEST_SW',
        'mgmt_ip': '10.0.0.1',
        'site': 'LAB',
        'role': 'access',
        'os_type': 'cisco_ios',
        'vendor': None,
        'os_version': None,
        'model': None,
        'serial_number': None,
        'collected_os_version': None,
        'uptime': None,
        'last_scanned': None,
        'scan_status': None
    }
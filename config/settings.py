import yaml
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def load_yaml_inventory(path=None):
    if path is None:
        # Default behavior - user config/devices.yaml
        config_dir = Path(__file__).parent
        yaml_path = config_dir / "devices.yaml"
    else:
        yaml_path = Path(path)
    if not yaml_path.exists():
        print("File does not exist")
        raise FileNotFoundError(f"Cannot find {yaml_path}")
    with open(yaml_path, "r") as f:
        raw_data = yaml.safe_load(f)
        return raw_data.get("devices", [])

def load_dotenv_values():
    username = os.environ.get("DEFAULT_USERNAME")
    password = os.environ.get("DEFAULT_PASSWORD")
    return username, password

def get_device_credentials(device):
    """
    Get credentials for a device.
    Works with both dictionaries (from YAML) and Device objects.
    
    Args:
        device: Either a dict or Device object
        
    Returns:
        tuple: (username, password)
    """
    username = None
    password = None
    
    # Check if it's a dictionary or an object
    if isinstance(device, dict):
        # Dictionary from YAML
        device_username = device.get("username")
        device_password = device.get("password")
        device_hostname = device.get("hostname")
    else:
        # Device object
        device_username = getattr(device, 'username', None)
        device_password = getattr(device, 'password', None)
        device_hostname = device.hostname
    
    # Get username (device-specific or default)
    if not device_username:
        username = os.environ.get("DEFAULT_USERNAME")
    else:
        # Device has custom username env var reference
        value = os.environ.get(device_username)
        if not value:
            print(f"No environment variable matching {device_username} for {device_hostname}")
            username = None
        else:
            username = value
    
    # Get password (device-specific or default)
    if not device_password:
        password = os.environ.get("DEFAULT_PASSWORD")
    else:
        # Device has custom password env var reference
        value = os.environ.get(device_password)
        if not value:
            print(f"No environment variable matching {device_password} for {device_hostname}")
            password = None
        else:
            password = value
    
    return username, password

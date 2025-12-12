import yaml
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def load_yaml_inventory():
    config_dir = Path(__file__).parent
    yaml_path = config_dir / "devices.yaml"
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
    print(f"TSHOOT {device}")
    return "HELLO", "BONJOUR"
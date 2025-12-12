from src.models.device import Device
from config.settings import list_from_yaml

def InventoryManager():
    devices = list_from_yaml()
    for each in devices:
        print(each)
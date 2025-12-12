import json
from datetime import datetime
from pathlib import Path


def save_inventory_to_json(devices, count, output_dir="output"):

    timestamp = datetime.now()

    project_dir = Path(__file__).parent.parent.parent
    output_path = project_dir / output_dir
    output_path.mkdir(parents=True, exist_ok=True)

    filename = f"inventory_{timestamp.strftime('%Y%m%d_%H%M%S')}.json"
    filepath = output_path / filename

    list_device = []

    for each in devices:
        list_device.append(each.to_dict())

    output_data = {
        "metadata": {
            "generated_at": timestamp.isoformat(),
            "device_count": count,
            "version": "1.0"
        },
        "devices": list_device
    }

    with open(filepath, "w") as f:
        json.dump(output_data, f, indent=2)
    
    print(f"\n Inventory saved to : {filepath}")
    return filepath
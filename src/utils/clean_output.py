from pathlib import Path
import os

root_path = Path(__file__).parent.parent.parent
output_path = root_path / "output"


print(output_path)

for each in output_path.iterdir():
    if str(each)[-5:] == ".json":
        print(each)
        os.remove(each)
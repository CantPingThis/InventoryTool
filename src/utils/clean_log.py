from pathlib import Path
import os

root_path = Path(__file__).parent.parent.parent
log_path = root_path / "logs"

for each in log_path.iterdir():
    if str(each)[-4:] == ".log":
        print(each)
        os.remove(each)

print("Logs files cleared")
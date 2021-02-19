import os
import subprocess
import yaml
from pathlib import Path

def  main():
    file_path = os.environ.get("INPUT_FILE_PATH")
    if file_path:
        path = Path(file_path)
        status_json = yaml.load(path.open(), Loader=yaml.SafeLoader)
        args = ["echo", "::set-output", f"name=status::{status_json['status']}"]
        subprocess.call(args)
    else:
        print("file_path not found.")


if __name__ == "__main__":
    main()

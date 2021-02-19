import os
import subprocess
import yaml
from pathlib import Path

def  main():
    file_path = os.environ.get("INPUT_FILE_PATH")
    status = 'n/a'
    if file_path:
        path = Path(file_path)
        status_json = yaml.load(path.open(), Loader=yaml.SafeLoader)
        status = status_json['status']
    else:
        print("file_path not found.")
    
    args = ["echo", "::set-output", f"name=status::{status}"]
    subprocess.call(args)


if __name__ == "__main__":
    main()

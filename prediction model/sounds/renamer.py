import os
from pathlib import Path

dir_path = "."

def renamer():
    for entry in os.scandir(dir_path):
        if entry.is_dir():
            continue
        file_path = Path(entry)
        if file_path == "renamer.py":
            continue
        final_file_format = file_path.suffix.lower()
        parts = str(file_path).split(".")
        parts = parts[0].split("__")
        print(parts)
        file_path.rename((parts[2] + final_file_format))

if __name__ == "__main__":
    renamer()
        
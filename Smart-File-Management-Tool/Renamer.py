# renamer.py
import os
from utils.logger import log

def bulk_rename(folder_path, prefix="file", start_num=1, suffix=""):
    """
    Bulk rename files in a folder with optional prefix, suffix, and numbering.
    """
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for i, file in enumerate(files, start=start_num):
        ext = os.path.splitext(file)[1]
        new_name = f"{prefix}{i}{suffix}{ext}"
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        log(f"Renamed {old_path} → {new_path}")
    print(f"{len(files)} files renamed successfully.")

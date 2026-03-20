import os
import shutil
from utils.logger import log

def move_file(src_path, dest_folder):
    """
    Move file to dest_folder. Handles duplicates automatically.
    """
    os.makedirs(dest_folder, exist_ok=True)
    filename = os.path.basename(src_path)
    dest_path = os.path.join(dest_folder, filename)
    count = 1
    while os.path.exists(dest_path):
        name, ext = os.path.splitext(filename)
        dest_path = os.path.join(dest_folder, f"{name}_{count}{ext}")
        count += 1
    shutil.move(src_path, dest_path)
    log(f"Moved {src_path} → {dest_path}")

def copy_file(src_path, dest_folder):
    """
    Copy file to dest_folder. Handles duplicates automatically.
    """
    os.makedirs(dest_folder, exist_ok=True)
    filename = os.path.basename(src_path)
    dest_path = os.path.join(dest_folder, filename)
    count = 1
    while os.path.exists(dest_path):
        name, ext = os.path.splitext(filename)
        dest_path = os.path.join(dest_folder, f"{name}_{count}{ext}")
        count += 1
    shutil.copy2(src_path, dest_path)
    log(f"Copied {src_path} → {dest_path}")

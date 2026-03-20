# backup.py
import os
import shutil
from datetime import datetime
from utils.logger import log

def backup_folder(src_folder):
    """
    Create a backup of the given folder.
    Backup folder is created with date-time stamp.
    """
    if not os.path.exists(src_folder):
        print("Source folder does not exist.")
        return
    
    base_name = os.path.basename(os.path.normpath(src_folder))
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder_name = f"{base_name}_backup_{timestamp}"
    dest_folder = os.path.join(os.path.dirname(src_folder), backup_folder_name)
    
    try:
        shutil.copytree(src_folder, dest_folder)
        log(f"Backup created: {dest_folder}")
        print(f"Backup successful → {dest_folder}")
    except Exception as e:
        log(f"Backup failed: {e}")
        print(f"Backup failed: {e}")

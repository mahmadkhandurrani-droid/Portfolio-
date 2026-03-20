from utils.file_ops import move_file
from utils.logger import log
import os

def organize_folder(folder_path):
    """
    Organize files in folder by their extension into subfolders.
    """
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            ext = item.split('.')[-1]
            dest = os.path.join(folder_path, ext.upper() + "_files")
            move_file(item_path, dest)
    log(f"Organized folder: {folder_path}")
    print("Folder organized successfully.")

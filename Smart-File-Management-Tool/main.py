from organizer import organize_folder
from backup import backup_folder
from renamer import bulk_rename
from folder_report import generate_report
from utils.logger import log

def main_menu():
    """
    Central nested menu for Smart File Management Tool
    """
    while True:
        print("\n--- Smart File Management Tool ---")
        print("1. File Organizer")
        print("2. Backup Script")
        print("3. Bulk File Renamer")
        print("4. Folder Report Generator")
        print("5. Exit")
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            folder = input("Enter folder path to organize: ").strip()
            organize_folder(folder)
        elif choice == "2":
            src = input("Enter folder path to backup: ").strip()
            backup_folder(src)
        elif choice == "3":
            folder = input("Enter folder to rename files in: ").strip()
            bulk_rename(folder)
        elif choice == "4":
            folder = input("Enter folder for report: ").strip()
            generate_report(folder)
        elif choice == "5":
            log("Exited Smart File Management Tool")
            break
        else:
            print("Invalid choice. Try again.")

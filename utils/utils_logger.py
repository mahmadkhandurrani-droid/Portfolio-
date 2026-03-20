import datetime
import os

LOG_FILE = "logs/log.txt"
os.makedirs("logs", exist_ok=True)

def log(message):
    """
    Central logging function.
    Writes message with timestamp to log.txt
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

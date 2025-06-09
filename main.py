import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore
import threading
import time
import os
import sys

init(autoreset=True)
print_lock = threading.Lock()

checked = 0
valid_count = 0
start_time = None

def set_terminal_title(title):
    if os.name == 'nt':
        safe_title = title.replace(":", "-").replace("|", "-")
        os.system(f"title {safe_title}")
    else:
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

def log_result(status, username):
    status_label = f"[{status}]".ljust(7)
    username_field = username.ljust(10)
    with print_lock:
        if status == "VALID":
            print(Fore.GREEN + f"{status_label} {username_field}")
        else:
            print(Fore.RED + f"{status_label} {username_field}")

def check_username(username):
    global checked, valid_count
    url = f"https://auth.roblox.com/v1/usernames/validate?Username={username}&Birthday=2000-01-01"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 429:
    
            time.sleep(2)
            response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            message = data.get("message", "").strip().lower()
            if message == "username is valid":
                with print_lock:
                    valid_count += 1
                return username, True
            else:
                return username, False
        else:
            return username, False
    except Exception:
        return username, False
    finally:
        time.sleep(0.10) 

def process_username(username):
    global checked, start_time
    username, is_available = check_username(username)
    with print_lock:
        checked += 1
        elapsed = max(time.time() - start_time, 1)
        cpm = int((checked / elapsed) * 60)
        set_terminal_title(f"roblox sniper - Checked: {checked} | Valid: {valid_count} | CPM: {cpm}")

    if is_available:
        log_result("VALID", username)
        with open("valid.txt", "a") as valid_file:
            valid_file.write(f"{username}\n")
    else:
        log_result("TAKEN", username)
        with open("invalid.txt", "a") as invalid_file:
            invalid_file.write(f"{username}\n")

def main():
    global start_time

    print("="*40)
    print("     roblox sniper  ")
    print("="*40)

    webhook_choice = input("Do you want to send results to a webhook? (y/n): ").strip().lower()
    if webhook_choice == 'y':
        webhook_url = input("Enter webhook URL: ").strip()
        print("Webhook feature not implemented yet, but URL saved.")
    else:
        webhook_url = None

    start_choice = input("Start sniping now? (y/n): ").strip().lower()
    if start_choice != 'y':
        print("Exiting...")
        return

    open("valid.txt", "w").close()
    open("invalid.txt", "w").close()

    with open("usernames.txt", "r") as f:
        usernames = [line.strip() for line in f if line.strip()]

    start_time = time.time()

    max_threads = 10 # adjust as needed

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(process_username, usernames)

    print("\nFinished checking all usernames.")

if __name__ == "__main__":
    main()

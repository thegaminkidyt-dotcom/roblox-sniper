import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore
from datetime import datetime
import threading
import time
import os
import sys
import argparse
import json

init(autoreset=True)
print_lock = threading.Lock()

checked = 0
valid_count = 0
start_time = None
webhook_url = "WEBHOOK_URL_HERE"  # Replace with your actual webhook URL

def set_terminal_title(title):
    if os.name == 'nt':
        safe_title = title.replace(":", "-").replace("|", "-")
        os.system(f"title {safe_title}")
    else:
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

def send_webhook(webhook_url, username):
    try:
        payload = {
            "content": f"✅ **Valid Username Found:** `{username}`"
        }
        headers = {"Content-Type": "application/json"}
        requests.post(webhook_url, data=json.dumps(payload), headers=headers, timeout=5)
    except Exception as e:
        with print_lock:
            print(Fore.YELLOW + f"[ERROR] Webhook failed: {e}")

def log_result(status, username):
    status_label = f"[{status}]".ljust(7)
    username_field = username.ljust(10)
    with print_lock:
        if status == "VALID":
            print(Fore.GREEN + f"{status_label} {username_field}")
        else:
            print(Fore.RED + f"{status_label} {username_field}")

def check_username(username):
    url = f"https://auth.roblox.com/v1/usernames/validate?Username={username}&Birthday=2000-01-01"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            message = data.get("message", "").strip().lower()
            return username, (message == "username is valid")
    except Exception as e:
        with print_lock:
            print(Fore.YELLOW + f"[ERROR] {username} - {e}")
    return username, False

def process_username(username):
    global checked, valid_count
    username, is_valid = check_username(username)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with print_lock:
        checked += 1
        if is_valid:
            valid_count += 1
        elapsed = max(time.time() - start_time, 1)
        cpm = int((checked / elapsed) * 60)
        set_terminal_title(f"RoSnipe: {checked} | Valid: {valid_count} | CPM: {cpm}")

    if is_valid:
        log_result("VALID", username)
        with open("valid.txt", "a") as vf:
            vf.write(f"[{timestamp}] {username}\n")
        send_webhook(webhook_url, username)
    else:
        log_result("TAKEN", username)
        with open("invalid.txt", "a") as inf:
            inf.write(f"[{timestamp}] {username}\n")

def main():
    global start_time

    print(Fore.RED + r"""

  _____   ____   _____ _   _ _____ _____  ______ _____  
 |  __ \ / __ \ / ____| \ | |_   _|  __ \|  ____|  __ \ 
 | |__) | |  | | (___ |  \| | | | | |__) | |__  | |__) |
 |  _  /| |  | |\___ \| . ` | | | |  ___/|  __| |  _  / 
 | | \ \| |__| |____) | |\  |_| |_| |    | |____| | \ \ 
 |_|  \_\\____/|_____/|_| \_|_____|_|    |______|_|  \_\
                                                        
                                                        

    """)

    parser = argparse.ArgumentParser()
    parser.add_argument("--threads", type=int, default=20, help="Number of threads (default 20)")
    args = parser.parse_args()

    start_choice = input("Start sniping now? (y/n): ").strip().lower()
    if start_choice != 'y':
        print("Exiting.")
        return

    open("valid.txt", "w").close()
    open("invalid.txt", "w").close()

    with open("usernames.txt", "r") as f:
        usernames = [line.strip() for line in f if line.strip()]

    max_threads = min(len(usernames), args.threads)
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(process_username, usernames)

    elapsed = round(time.time() - start_time, 2)
    print(Fore.CYAN + "\nSummary:")
    print(Fore.CYAN + f"Checked: {checked}")
    print(Fore.GREEN + f"Valid: {valid_count}")
    print(Fore.RED + f"Taken: {checked - valid_count}")
    print(Fore.CYAN + f"Time Elapsed: {elapsed} seconds")

if __name__ == "__main__":
    main()

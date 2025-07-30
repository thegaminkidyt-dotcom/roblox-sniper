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
import signal
from urllib.parse import quote

init(autoreset=True)
print_lock = threading.Lock()

# Global variables
checked = 0
valid_count = 0
start_time = None
webhook_url = "WEBHOOK_URL_HERE"  # Replace with your actual webhook URL
running = True

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    global running
    print(Fore.YELLOW + "\n[INFO] Stopping gracefully...")
    running = False

signal.signal(signal.SIGINT, signal_handler)

def set_terminal_title(title):
    """Set terminal title cross-platform"""
    if os.name == 'nt':
        safe_title = title.replace(":", "-").replace("|", "-")
        os.system(f"title {safe_title}")
    else:
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

def send_webhook(webhook_url, username):
    """Send Discord webhook notification for valid usernames"""
    if webhook_url == "WEBHOOK_URL_HERE":
        return  # Skip if webhook not configured
    
    try:
        payload = {
            "content": f"✅ **Valid Username Found:** `{username}`",
            "username": "RoSnipe Bot"
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers, timeout=10)
        
        if response.status_code == 429:  # Rate limited
            with print_lock:
                print(Fore.YELLOW + f"[WARNING] Webhook rate limited")
        elif response.status_code != 204:
            with print_lock:
                print(Fore.YELLOW + f"[WARNING] Webhook returned status {response.status_code}")
                
    except requests.exceptions.Timeout:
        with print_lock:
            print(Fore.YELLOW + f"[ERROR] Webhook timeout")
    except Exception as e:
        with print_lock:
            print(Fore.YELLOW + f"[ERROR] Webhook failed: {e}")

def log_result(status, username, message=""):
    """Log username check result with colored output"""
    status_label = f"[{status}]".ljust(8)
    username_field = username.ljust(15)
    message_field = message[:30] if message else ""
    
    with print_lock:
        if status == "VALID":
            print(Fore.GREEN + f"{status_label} {username_field} {message_field}")
        elif status == "TAKEN":
            print(Fore.RED + f"{status_label} {username_field} {message_field}")
        elif status == "ERROR":
            print(Fore.YELLOW + f"{status_label} {username_field} {message_field}")

def validate_username(username):
    """Validate username format before checking"""
    if not username:
        return False, "Empty username"
    if len(username) < 3 or len(username) > 20:
        return False, "Invalid length (3-20 chars)"
    if not username.replace('_', '').isalnum():
        return False, "Invalid characters"
    return True, ""

def check_username(username):
    """Check if username is available on Roblox"""
    # Validate username format first
    is_valid_format, error_msg = validate_username(username)
    if not is_valid_format:
        return username, False, error_msg
    
    # URL encode the username to handle special characters
    encoded_username = quote(username)
    url = f"https://auth.roblox.com/v1/usernames/validate?Username={encoded_username}&Birthday=2000-01-01"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            message = data.get("message", "").strip().lower()
            is_available = message == "username is valid"
            return username, is_available, message
        elif response.status_code == 429:
            return username, False, "Rate limited"
        else:
            return username, False, f"HTTP {response.status_code}"
            
    except requests.exceptions.Timeout:
        return username, False, "Timeout"
    except requests.exceptions.ConnectionError:
        return username, False, "Connection error"
    except Exception as e:
        return username, False, f"Error: {str(e)[:20]}"

def process_username(username):
    """Process a single username check"""
    global checked, valid_count, running
    
    if not running:
        return
    
    username, is_valid, message = check_username(username)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with print_lock:
        checked += 1
        if is_valid:
            valid_count += 1
        
        # Calculate stats
        elapsed = max(time.time() - start_time, 1)
        cpm = int((checked / elapsed) * 60)
        set_terminal_title(f"RoSnipe: {checked} | Valid: {valid_count} | CPM: {cpm}")

    # Log and save results
    if is_valid:
        log_result("VALID", username, message)
        with open("valid.txt", "a", encoding='utf-8') as vf:
            vf.write(f"[{timestamp}] {username}\n")
        send_webhook(webhook_url, username)
    elif "error" in message.lower() or "timeout" in message.lower():
        log_result("ERROR", username, message)
        with open("errors.txt", "a", encoding='utf-8') as ef:
            ef.write(f"[{timestamp}] {username} - {message}\n")
    else:
        log_result("TAKEN", username, message)
        with open("taken.txt", "a", encoding='utf-8') as tf:
            tf.write(f"[{timestamp}] {username} - {message}\n")

def load_usernames(filename):
    """Load usernames from file with error handling"""
    try:
        with open(filename, "r", encoding='utf-8') as f:
            usernames = [line.strip() for line in f if line.strip()]
        
        # Remove duplicates while preserving order
        seen = set()
        unique_usernames = []
        for username in usernames:
            if username.lower() not in seen:
                seen.add(username.lower())
                unique_usernames.append(username)
        
        print(Fore.CYAN + f"Loaded {len(unique_usernames)} unique usernames from {filename}")
        return unique_usernames
        
    except FileNotFoundError:
        print(Fore.RED + f"Error: {filename} not found!")
        print(Fore.YELLOW + f"Please create {filename} with one username per line.")
        return []
    except Exception as e:
        print(Fore.RED + f"Error reading {filename}: {e}")
        return []

def main():
    global start_time, webhook_url

    print(Fore.RED + r"""
  _____   ____   _____ _   _ _____ _____  ______ _____  
 |  __ \ / __ \ / ____| \ | |_   _|  __ \|  ____|  __ \ 
 | |__) | |  | | (___ |  \| | | | | |__) | |__  | |__) |
 |  _  /| |  | |\___ \| . ` | | | |  ___/|  __| |  _  / 
 | | \ \| |__| |____) | |\  |_| |_| |    | |____| | \ \ 
 |_|  \_\\____/|_____/|_| \_|_____|_|    |______|_|  \_\
                                                        
                     Enhanced Version v2.0                           
    """)

    parser = argparse.ArgumentParser(description="Roblox Username Availability Checker")
    parser.add_argument("--threads", type=int, default=20, help="Number of threads (default: 20)")
    parser.add_argument("--input", type=str, default="usernames.txt", help="Input file (default: usernames.txt)")
    parser.add_argument("--webhook", type=str, help="Discord webhook URL")
    parser.add_argument("--no-prompt", action="store_true", help="Skip confirmation prompt")
    args = parser.parse_args()

    # Set webhook URL if provided
    if args.webhook:
        webhook_url = args.webhook

    # Load usernames
    usernames = load_usernames(args.input)
    if not usernames:
        return

    # Confirmation prompt
    if not args.no_prompt:
        print(Fore.CYAN + f"Ready to check {len(usernames)} usernames with {args.threads} threads")
        start_choice = input("Start checking now? (y/n): ").strip().lower()
        if start_choice != 'y':
            print("Exiting.")
            return

    # Clear output files
    for filename in ["valid.txt", "taken.txt", "errors.txt"]:
        open(filename, "w", encoding='utf-8').close()

    print(Fore.CYAN + f"Starting username checker...")
    print(Fore.CYAN + f"Threads: {args.threads}")
    print(Fore.CYAN + f"Webhook: {'Enabled' if webhook_url != 'WEBHOOK_URL_HERE' else 'Disabled'}")
    print(Fore.CYAN + f"Press Ctrl+C to stop gracefully\n")

    # Start processing
    max_threads = min(len(usernames), args.threads)
    start_time = time.time()

    try:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            executor.map(process_username, usernames)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nStopped by user")

    # Final statistics
    elapsed = round(time.time() - start_time, 2)
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.CYAN + "FINAL SUMMARY")
    print(Fore.CYAN + "="*50)
    print(Fore.CYAN + f"Total Checked: {checked}")
    print(Fore.GREEN + f"Valid Available: {valid_count}")
    print(Fore.RED + f"Taken/Invalid: {checked - valid_count}")
    print(Fore.CYAN + f"Time Elapsed: {elapsed} seconds")
    print(Fore.CYAN + f"Average CPM: {int((checked / max(elapsed, 1)) * 60)}")
    print(Fore.CYAN + "="*50)
    
    if valid_count > 0:
        print(Fore.GREEN + f"✅ Found {valid_count} available usernames! Check valid.txt")
    else:
        print(Fore.YELLOW + "❌ No available usernames found")

if __name__ == "__main__":
    main()
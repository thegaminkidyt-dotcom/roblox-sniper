Roblox Username Sniper

A fast, multithreaded Roblox username availability checker written in Python.  
Designed to quickly verify large lists of potential usernames by querying Roblox’s official API.
Weather you're using this tool to create burner accounts with your desired username, please use this carefully.

---

## Features

- **Multithreaded** for faster username checking using Python’s `ThreadPoolExecutor`  
- Displays **real-time progress** with checked count and CPM (checks per minute) in the terminal window title  
- Color-coded terminal output:  
  - **Green** for valid (available) usernames  
  - **Red** for taken usernames  
- Saves results to `valid.txt` and `invalid.txt` files  
- Handles API rate limiting gracefully with retries and throttling  
- Interactive terminal prompts to start checking and optionally enter a webhook URL (webhook functionality not yet implemented)  
- Simple to use and easy to customize  

---

## Requirements

- Python 3.x  
- [requests](https://pypi.org/project/requests/)  
- [colorama](https://pypi.org/project/colorama/)  

Install dependencies using pip:

```bash
pip install requests colorama


Usage
Create a usernames.txt file in the same directory with one username per line to check.

Run the script:

bash
Copy
Edit
python roblox_checker.py
Follow the prompts in the terminal:

Choose whether to enter a webhook URL (functionality coming soon)

Confirm if you want to start sniping

The script will check each username and output the results in the terminal with colors and save to:

valid.txt (available usernames)

invalid.txt (taken or invalid usernames)

Notes
To avoid rate limits and IP bans, the script includes a small delay and retries on rate limiting.

Adjust the number of threads in the script (max_threads variable) based on your internet speed and tolerance to rate limits.

Disclaimer
This tool is intended for educational and personal use only.
Respect Roblox's API usage policies and terms of service.
Excessive or abusive usage may lead to temporary or permanent bans.

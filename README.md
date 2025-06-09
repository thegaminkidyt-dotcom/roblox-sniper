# dizzyman0 Roblox Username Sniper

A fast, multithreaded Roblox username availability checker written in Python.  
Designed to quickly verify large lists of potential usernames by querying Roblox’s official API.

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




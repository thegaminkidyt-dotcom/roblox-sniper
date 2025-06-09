# dizzyman0 Roblox Username Sniper

A fast, open source, multithreaded Roblox username availability checker written in Python.  
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

## Usage

1. Create a folder and place all script files into it.  
2. Add your desired usernames to the `usernames.txt` file (one username per line).  
3. Open the folder, click the path bar, type `cmd`, and press Enter — this opens a terminal at your project folder.  
4. Run the script by typing:  
   ```bash
   python main.py

## dizzyman0 Roblox Username Sniper

A fast, open source, multithreaded Roblox username availability checker written in Python.  
Designed to quickly verify large lists of potential usernames by querying Roblox’s official API.

---

## Features

- **Multithreaded** for faster username checking using Python’s \`ThreadPoolExecutor\`  
- Displays **real-time progress** with checked count and CPM (checks per minute) in the terminal window title  
- Color-coded terminal output:  
  - **Green** for valid (available) usernames  
  - **Red** for taken usernames  
- Saves results to \`valid.txt\` and \`invalid.txt\` files  
- Handles API rate limiting gracefully with retries and throttling  
- Interactive terminal prompts to start checking and optionally enter a webhook URL (webhook functionality not yet implemented)  
- Simple to use and easy to customize  

---

## Usage

1. Create a folder and place all script files into it.  
2. Add your desired usernames to the \`usernames.txt\` file (one username per line).  
3. Open the folder, click the path bar, type \`cmd\`, and press Enter — this opens a terminal at your project folder.  
4. Run the script by typing:  
   python main.py
5. Follow the instructions in the terminal.  
6. Enjoy your sniping!  

---

## Requirements

- Python 3.x  
- [requests](https://pypi.org/project/requests/)  
- [colorama](https://pypi.org/project/colorama/)  

Install dependencies using pip:


pip install requests colorama

---

## Notes

- To avoid rate limits and IP bans, the script includes a small delay and retries on rate limiting.  
- Adjust the number of threads in the script (\`max_threads\` variable) based on your internet speed and tolerance to rate limits.  

---

## Disclaimer

This tool is intended for educational and personal use only.  
Respect Roblox's API usage policies and terms of service.  
Excessive or abusive usage may lead to temporary or permanent bans.

---

## License

MIT License © dizzyman0

---

Feel free to messege me with any errors you're having or any suggestions!" > README.md

Discord: @vzfl

# 🎯 dizzyman0 Roblox Username Sniper

A blazing-fast, multithreaded, open-source Roblox username checker written in Python.  
Designed to quickly verify large lists of potential usernames using Roblox's official API.

![Script in Action](https://cdn.discordapp.com/attachments/1381740628735430678/1381742142040571954/image.png?ex=68489f26&is=68474da6&hm=8eb919f82ef6b48801819b7640100d5364149428da32ec1cfb2bf38b3fde7806&)

---

## ⚡ Features

- ✅ **Multithreaded** — lightning-fast checks with `ThreadPoolExecutor`
- ✅ Displays **live progress** in the terminal title:
  - `Checked`, `Valid`, and **CPM** (Checks Per Minute)
- ✅ **Color-coded terminal output**:
  - 🟩 Green: username is available
  - 🟥 Red: username is taken
- ✅ Saves results:
  - `valid.txt` — available usernames
  - `invalid.txt` — taken usernames
- ✅ Interactive terminal prompts:
  - Ask to send results to a webhook (future feature)
  - Ask to start sniping
- ✅ Automatically handles slowdowns and retries (basic anti-rate-limit logic)
- ✅ Beginner-friendly, portable, and lightweight

---

## 🛠️ Requirements
- IMPORTANT NOTE: YOU MUST INSTALL PYTHON TO PATH WHEN INSTALLING
- Python 3.7 or higher  
- Packages:
  - `requests`
  - `colorama`

Install with Python:

pip install colorama requests

---


## 🚀 Usage

1. **Clone or download** the repository files into a folder.
2. Open `usernames.txt` and paste your list of usernames (one per line).
3. Open the folder in File Explorer.
4. In the top bar, type `cmd` and press Enter to open a terminal in that folder.
5. Run the script:

```bash
python main.py

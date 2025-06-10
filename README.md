# 🎯 dizzyman0 Roblox Username Sniper

A blazing-fast, multithreaded, open-source Roblox username checker written in Python.  
Designed to quickly verify large lists of potential usernames using Roblox's official API.

![Script in Action](https://media.discordapp.net/attachments/1257226957888684125/1381885478940180601/Screenshot_2025-06-09_233649.png?ex=684924a4&is=6847d324&hm=bf0beab148741605bc1224bec291f9cfcbd9ec5fad7dd6f7740d4b3f42193c1c&=&format=webp&quality=lossless&width=625&height=557)

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
---


** Questions or concerns

Messege me on discord @vzfl

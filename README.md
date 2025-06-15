Sure! Here’s the full clean copy-paste version of your README that you can use anywhere (Discord, GitHub, Notepad, etc.):

⸻


# 🎯 Roblox Username Sniper

A **blazing-fast**, multithreaded, open-source Roblox username checker written in Python.  
Designed to quickly verify large lists of potential usernames using Roblox’s official API.

![Script in Action](https://media.discordapp.net/attachments/1257226957888684125/1381885478940180601/Screenshot_2025-06-09_233649.png?ex=684924a4&is=6847d324&hm=bf0beab148741605bc1224bec291f9cfcbd9ec5fad7dd6f7740d4b3f42193c1c&=&format=webp&quality=lossless&width=625&height=557)

---

## ⚡ Features

✅ **Multithreaded** — lightning-fast checks using `ThreadPoolExecutor`  
✅ Displays **live progress** in the terminal title (Checked, Valid, CPM)  
✅ **Color-coded output**:
- 🟩 Green = Available
- 🟥 Red = Taken  
✅ Saves results:
- `valid.txt` (available usernames)
- `invalid.txt` (taken usernames)  
✅ **Interactive terminal prompts**:
- Optionally send results to a Discord webhook
- Optionally start sniping  
✅ Basic anti-rate-limit handling (slowdown detection + retries)  
✅ Lightweight, beginner-friendly, and portable

---

## 🛠️ Requirements

➡ **Install Python 3.7+**  
➡ Make sure you select **Add Python to PATH** when installing!

➡ Required Python packages:
```bash
pip install requests colorama


⸻

🚀 Usage

1️⃣ Clone or download the files into a folder.
2️⃣ Open usernames.txt and paste your list of usernames (one per line).
3️⃣ Open the folder in File Explorer.
4️⃣ In the top bar, type cmd and press Enter.
5️⃣ Run the script:

python main.py


⸻

💬 Need help or have suggestions?
Message me on Discord: @vzfl

---

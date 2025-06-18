
# 🎯 RoSnipe

A **blazing-fast**, multithreaded, open-source Roblox username checker written in Python.  
Designed to quickly verify large lists of potential usernames using Roblox’s official API.
![Screenshot](https://cdn.discordapp.com/attachments/1257226957888684125/1381885478940180601/Screenshot_2025-06-09_233649.png?ex=685064e4&is=684f1364&hm=9890cb72c3f3a3cd266ed2a9c43230638102eb9a9983ccf38ded550b26bb4cad&)
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
- ** Code Text Editor (Visual Studio Code recommended)
➡ **Install Python 3.7+**  
➡ Make sure you select **Add Python to PATH** when installing!

➡ Required Python packages:

pip install requests colorama

---

## 🚀 Usage

1️⃣ Clone or download the files into a folder.  
2️⃣ Open `usernames.txt` and paste your list of usernames (one per line).  
3️⃣ Open the folder in File Explorer.  
4️⃣ In the top bar, type `cmd` and press **Enter**.  
5️⃣ Run the script:

python main.py

---

💬 **Need help or have suggestions?**  
Message me on Discord: `@vzfl`

<div align="center">

# 🗂️ Python Folder Organizer

**Tidy any messy folder in one command - files are sorted into sub-folders by their extension.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-batch_launcher-0078D6?logo=windows&logoColor=white)

</div>

---

## ✨ How it works

Give it a folder path and it:

1. 🔍 Finds every file extension in that folder.
2. 📁 Creates one sub-folder per extension (`pdf/`, `jpg/`, `txt/`, ...).
3. 🚚 Moves each file into the folder matching its extension.

## 🚀 Getting Started

### Run directly

```bash
git clone https://github.com/Arashomranpour/python-organizer.git
cd python-organizer
python organizer.py
# Enter a path : C:\Users\you\Downloads
```

### Run it as a global command (Windows)

1. Edit `organizer.bat` so it points to the full path of `organizer.py`.
2. Copy `organizer.bat` into a folder on your `PATH` (for example `C:\Windows\System32`).
3. Open `cmd` anywhere and type:

```bat
organizer
```

> ⚠️ Files are **moved**, not copied. Try it on a test folder first.

## 📁 Project Structure

```
.
├── organizer.py    # Sorting logic
└── organizer.bat   # Windows launcher
```

## 🛠️ Tech Stack

`Python` · `os` · `shutil`

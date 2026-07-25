# Mouse POS Saver & Teleporter

A lightweight Python utility for Windows 11 that lets you save your mouse cursor's exact screen coordinates with a single hotkey, then instant-teleport your cursor back to those coordinates whenever needed.

---

## Features

- **Instant Coordinate Saving:** Press a key combination to capture your current `(X, Y)` screen location.
- **Persistent Memory:** Teleport as many times as you want without losing your saved position.
- **Global Hotkeys:** Works seamlessly across Windows 11, even while playing games or tabbed into other applications.
- **Real-Time CMD Output:** Live terminal dashboard that displays active hotkeys and current saved coordinates.

---

## Hotkeys

| Action | Default Keybind | Description |
| :--- | :--- | :--- |
| **Save Position** | `Ctrl` + `Alt` + `S` | Saves current mouse `(X, Y)` position |
| **Teleport Mouse** | `Ctrl` + `Alt` + `T` | Instantly moves cursor to saved position |
| **Exit Script** | `Ctrl` + `Alt` + `Q` | Safely closes the application |

*(Keybinds can be customized directly inside the `mouse_tp.py` file.)*

---

## Step-by-Step Setup Guide

Follow these steps to set up and run the project from scratch on Windows 11:

### Step 1: Install Python
1. Download Python from [python.org](https://www.python.org/downloads/).
2. Run the installer and **check the box** that says **"Add python.exe to PATH"** before clicking Install.

### Step 2: Create Your Script File
1. Create a new folder on your computer (e.g., `C:\MouseTeleporter`).
2. Inside that folder, create a new file or download the file named `mouse_tp.py`.
3. Open `mouse_tp.py` with Notepad or any text editor, paste the Python code into it, and save. (If you created it by yourself)

### Step 3: Install Required Dependencies
1. Press `Win + S`, type `cmd`, right-click **Command Prompt**, and select **Run as administrator**.
2. Run the following command:
   ```cmd
   pip install pyautogui keyboard

### Step 4: Run
1. Go to the folder that have the python file in it with the **Administrator Command Prompt** by running cd "C:\Users\user\folder\your folder"
3. Run `python mouse_tp.py` in the **Administrator Command Prompt**
4. Or just run the file as **Administrator**

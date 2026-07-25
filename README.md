# Mouse POS Saver & Teleporter

A lightweight Windows 11 desktop widget built with Python and Tkinter. It lets you save your mouse cursor's exact screen coordinates with a hotkey and instant-teleport back to them anytime via a clean, floating dark-mode overlay window—no ugly console needed!

---

## Features

- **Floating Dark Theme Overlay:** Stays on top of games and apps so you can always check your saved coordinates.
- **Instant Coordinate Saving:** Press a quick shortcut to snapshot your `(X, Y)` cursor position.
- **Persistent Memory:** Teleport as many times as you want without losing your target point.
- **Global Hotkeys:** Works across all Windows 11 applications, games, and full-screen windows.
- **Console-Free:** Runs cleanly as a native desktop window using `.pyw`.

---

## Hotkeys

| Action | Default Keybind | Description |
| :--- | :--- | :--- |
| **Save Position** | `Ctrl` + `Alt` + `S` | Captures current mouse `(X, Y)` position |
| **Teleport Mouse** | `Ctrl` + `Alt` + `T` | Instantly moves cursor to saved position |

*(Keybinds can be easily customized directly inside the script!)*

---

## Step-by-Step Setup Guide

Follow these steps to set up and run the project from scratch on Windows 11:

### Step 1: Install Python
1. Download Python from [python.org](https://www.python.org/downloads/).
2. Run the installer and **make sure to check the box** that says **"Add python.exe to PATH"** before clicking Install.

### Step 2: Create Your Script File
1. Create a new folder on your computer (e.g., `C:\MouseTeleporter`).
2. Inside that folder, download file named `mouse_tp_gui.pyw`.

### Step 3: Install Required Dependencies
1. Press `Win + S`, type `cmd`, right-click **Command Prompt**, and select **Run as administrator**.
2. Run the following command:
   ```cmd
   pip install pyautogui keyboard

### Step 4: Run
1. Just run the script as **Administrator**

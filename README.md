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

## Setup & Installation

### 1. Prerequisites
- **OS:** Windows 11
- **Python 3.x:** Ensure Python is installed and added to your system `PATH`.

### 2. Install Required Dependencies
Open **Command Prompt** or **Terminal** as **Administrator** and run:

```cmd
pip install pyautogui keyboard

# Mouse POS Saver & Teleporter

A sleek, modern Windows 11 desktop widget built with Python and CustomTkinter. It lets you save your mouse cursor's exact screen coordinates with global hotkeys (or UI buttons) and instant-teleport back to them anytime via a clean, floating dark-mode overlay window.

---

## Features

- **Modern Windows 11 UI:** Dark-mode card layout with rounded corners, custom badging, and smooth typography.
- **Floating Overlay:** Stays on top of apps and games (`topmost`) so you can inspect your saved target at any time.
- **Global Hotkeys:** Works seamlessly across Windows 11 using native Win32 API calls—no extra key-logging drivers needed.
- **Manual Action Buttons:** Trigger saves or teleports directly from the interface if you prefer clicking.
- **No Admin Required:** Runs as a standard background app without requiring elevated admin permissions.
- **Console-Free:** Launches cleanly as a native desktop utility via `.pyw`.

---

## Hotkeys

| Action | Default Keybind | Description |
| :--- | :--- | :--- |
| **Save Position** | `Ctrl` + `Alt` + `S` | Captures your current mouse `(X, Y)` position |
| **Teleport Mouse** | `Ctrl` + `Alt` + `T` | Instantly teleports cursor to saved coordinates |

---

## Step-by-Step Setup Guide

Follow these steps to set up and run the project on Windows 11:

### Step 1: Install Python
1. Download Python from [python.org](https://www.python.org/downloads/).
2. Run the installer and **make sure to check the box** that says **"Add python.exe to PATH"** before clicking Install.

### Step 2: Download the Script
1. Create a new folder on your computer (e.g., `C:\MouseTeleporter`).
2. Save your script inside that folder as `mouse_teleporter.pyw`.

### Step 3: Install Required Dependencies
Open **Command Prompt** or **PowerShell** and run:

```cmd
pip install customtkinter

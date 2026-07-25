import threading
import tkinter as tk
import keyboard
import pyautogui

# Global variables
saved_position = None

# --- CONFIGURATION (Hotkeys) ---
HOTKEY_SAVE = "ctrl+alt+s"
HOTKEY_TELEPORT = "ctrl+alt+t"


class MouseApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Teleporter")

        # Window properties: Always on top, clean dark theme, fixed size
        self.root.attributes("-topmost", True)
        self.root.configure(bg="#1e1e2e")
        self.root.geometry("320x220")
        self.root.resizable(False, False)

        # Title Label
        self.title_label = tk.Label(
            root,
            text="Mouse POS Saver",
            font=("Segoe UI", 14, "bold"),
            fg="#cdd6f4",
            bg="#1e1e2e",
        )
        self.title_label.pack(pady=(12, 5))

        # Status / Coordinates Display Box
        self.status_frame = tk.Frame(root, bg="#313244", bd=1, relief="flat")
        self.status_frame.pack(padx=15, pady=5, fill="x")

        self.pos_label = tk.Label(
            self.status_frame,
            text="Status: No position saved",
            font=("Segoe UI", 10, "bold"),
            fg="#f38ba8",
            bg="#313244",
            pady=10,
        )
        self.pos_label.pack()

        # Keybind Guide Section
        self.keybind_frame = tk.Frame(root, bg="#1e1e2e")
        self.keybind_frame.pack(pady=10)

        self.save_txt = tk.Label(
            self.keybind_frame,
            text=f"Save Hotkey:  {HOTKEY_SAVE.upper()}",
            font=("Segoe UI", 9),
            fg="#a6adc8",
            bg="#1e1e2e",
        )
        self.save_txt.pack(anchor="w")

        self.tp_txt = tk.Label(
            self.keybind_frame,
            text=f"Teleport Hotkey:  {HOTKEY_TELEPORT.upper()}",
            font=("Segoe UI", 9),
            fg="#a6adc8",
            bg="#1e1e2e",
        )
        self.tp_txt.pack(anchor="w")

        # Start keyboard hotkey listeners in a background thread
        threading.Thread(target=self.start_hotkeys, daemon=True).start()

    def update_status(self, text, color="#a6e3a1"):
        """Safely updates GUI text from hotkey events."""
        self.root.after(0, lambda: self.pos_label.config(text=text, fg=color))

    def save_pos(self):
        global saved_position
        saved_position = pyautogui.position()
        self.update_status(
            f"Saved: X={saved_position.x}, Y={saved_position.y}",
            color="#a6e3a1",
        )

    def teleport_pos(self):
        if saved_position is None:
            self.update_status("Error: Save a position first!", color="#f38ba8")
        else:
            pyautogui.moveTo(saved_position.x, saved_position.y)
            self.update_status(
                f"Teleported to: ({saved_position.x}, {saved_position.y})",
                color="#89b4fa",
            )

    def start_hotkeys(self):
        keyboard.add_hotkey(HOTKEY_SAVE, self.save_pos)
        keyboard.add_hotkey(HOTKEY_TELEPORT, self.teleport_pos)
        keyboard.wait()


if __name__ == "__main__":
    root = tk.Tk()
    app = MouseApp(root)
    root.mainloop()

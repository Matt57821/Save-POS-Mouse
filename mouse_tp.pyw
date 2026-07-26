import ctypes
from ctypes import wintypes
import sys
import threading
import time
import customtkinter as ctk

# Enable High-DPI Awareness for Windows 11 crisp rendering
if sys.platform == "win32":
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

# Win32 API structures and functions
user32 = ctypes.windll.user32


class POINT(ctypes.Structure):
    _fields_ = [("x", wintypes.LONG), ("y", wintypes.LONG)]


def get_cursor_pos():
    pt = POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y


def set_cursor_pos(x, y):
    user32.SetCursorPos(x, y)


# Theme Configuration
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class MouseTeleporterApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("Mouse Teleporter")
        self.geometry("360x310")
        self.resizable(False, False)
        self.attributes("-topmost", True)  # Always on top

        self.saved_x = None
        self.saved_y = None

        self._build_ui()

        # Start hotkey listener thread
        threading.Thread(target=self._hotkey_listener, daemon=True).start()

    def _build_ui(self):
        # Header Title
        self.title_label = ctk.CTkLabel(
            self,
            text="Mouse Position Teleporter",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
        )
        self.title_label.pack(pady=(20, 15))

        # Coordinates Display Card
        self.card = ctk.CTkFrame(
            self, corner_radius=12, fg_color="#1E1E2E", border_width=1, border_color="#2E2E3E"
        )
        self.card.pack(padx=20, pady=5, fill="x")

        self.status_title = ctk.CTkLabel(
            self.card,
            text="SAVED COORDINATES",
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="#A6ADC8",
        )
        self.status_title.pack(pady=(12, 2))

        self.pos_display = ctk.CTkLabel(
            self.card,
            text="No Position Saved",
            font=ctk.CTkFont(family="Consolas", size=18, weight="bold"),
            text_color="#F38BA8",
        )
        self.pos_display.pack(pady=(2, 12))

        # Keybind Badges Container
        self.keybind_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.keybind_frame.pack(pady=15)

        # Save Keybind Pill
        self._create_hotkey_pill(
            self.keybind_frame, label_text="SAVE", key_text="Ctrl + Alt + S"
        )

        # Teleport Keybind Pill
        self._create_hotkey_pill(
            self.keybind_frame, label_text="TELEPORT", key_text="Ctrl + Alt + T"
        )

        # Bottom Action / Manual Trigger Buttons
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=(5, 15), padx=20, fill="x")

        self.save_btn = ctk.CTkButton(
            self.btn_frame,
            text="Save Pos",
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color="#2B2D42",
            hover_color="#3D3F58",
            height=32,
            corner_radius=8,
            command=self.save_position,
        )
        self.save_btn.pack(side="left", expand=True, padx=(0, 5), fill="x")

        self.tp_btn = ctk.CTkButton(
            self.btn_frame,
            text="Teleport",
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color="#3B8ED0",
            hover_color="#1F6AA5",
            height=32,
            corner_radius=8,
            command=self.teleport_position,
        )
        self.tp_btn.pack(side="right", expand=True, padx=(5, 0), fill="x")

    def _create_hotkey_pill(self, parent, label_text, key_text):
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(pady=3, fill="x")

        lbl = ctk.CTkLabel(
            row,
            text=f"{label_text}:",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#89B4FA",
            width=70,
            anchor="e",
        )
        lbl.pack(side="left", padx=(0, 8))

        badge = ctk.CTkLabel(
            row,
            text=f" {key_text} ",
            font=ctk.CTkFont(family="Consolas", size=11, weight="bold"),
            fg_color="#313244",
            corner_radius=6,
            text_color="#CDD6F4",
        )
        badge.pack(side="left")

    def save_position(self):
        x, y = get_cursor_pos()
        self.saved_x = x
        self.saved_y = y
        self.after(
            0,
            lambda: self.pos_display.configure(
                text=f"X: {x} | Y: {y}", text_color="#A6E3A1"
            ),
        )

    def teleport_position(self):
        if self.saved_x is None or self.saved_y is None:
            self.after(
                0,
                lambda: self.pos_display.configure(
                    text="Save Position First!", text_color="#F38BA8"
                ),
            )
        else:
            set_cursor_pos(self.saved_x, self.saved_y)

    def _hotkey_listener(self):
        """Global Windows Hotkey polling thread using Win32 API."""
        VK_CONTROL = 0x11
        VK_MENU = 0x12  # Alt key
        VK_S = 0x53
        VK_T = 0x54

        s_pressed = False
        t_pressed = False

        while True:
            ctrl_down = bool(user32.GetAsyncKeyState(VK_CONTROL) & 0x8000)
            alt_down = bool(user32.GetAsyncKeyState(VK_MENU) & 0x8000)

            if ctrl_down and alt_down:
                # Check CTRL + ALT + S
                if user32.GetAsyncKeyState(VK_S) & 0x8000:
                    if not s_pressed:
                        s_pressed = True
                        self.save_position()
                else:
                    s_pressed = False

                # Check CTRL + ALT + T
                if user32.GetAsyncKeyState(VK_T) & 0x8000:
                    if not t_pressed:
                        t_pressed = True
                        self.teleport_position()
                else:
                    t_pressed = False
            else:
                s_pressed = False
                t_pressed = False

            time.sleep(0.03)


if __name__ == "__main__":
    app = MouseTeleporterApp()
    app.mainloop()

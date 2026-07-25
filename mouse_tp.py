import os
import time
import keyboard
import pyautogui

# Global variable to store saved mouse coordinates
saved_position = None

# --- CONFIGURATION (Change your hotkeys here) ---
HOTKEY_SAVE = "ctrl+alt+s"
HOTKEY_TELEPORT = "ctrl+alt+t"
HOTKEY_QUIT = "ctrl+alt+q"


def clear_console():
    """Clears the Command Prompt screen for a clean UI."""
    os.system("cls")


def print_dashboard():
    """Prints the current status, instructions, and hotkey guide."""
    clear_console()
    print("=" * 55)
    print("        MOUSE POSITION SAVER & TELEPORTER          ")
    print("=" * 55)
    print("WHAT THIS SCRIPT DOES:")
    print("  Allows you to snapshot your mouse cursor's exact (X, Y)")
    print("  screen coordinates using a hotkey, then teleport your mouse")
    print("  back to that saved position whenever you press another hotkey.")
    print("  Your saved position stays saved until you set a new one.")
    print("-" * 55)
    print("CONTROLS & KEYBINDS:")
    print(f"  [{HOTKEY_SAVE.upper():^12}] -> Save current mouse position")
    print(f"  [{HOTKEY_TELEPORT.upper():^12}] -> Teleport mouse to saved position")
    print(f"  [{HOTKEY_QUIT.upper():^12}] -> Quit script")
    print("-" * 55)

    if saved_position:
        x, y = saved_position
        print(f"STATUS: Saved Position -> X: {x}, Y: {y}")
    else:
        print("STATUS: No position saved yet.")

    print("=" * 55)
    print("\nListening for hotkeys...")


def save_mouse_pos():
    """Captures current mouse location."""
    global saved_position
    saved_position = pyautogui.position()
    print_dashboard()
    print(
        f"\n[SUCCESS] Mouse position saved at X: {saved_position.x}, Y: {saved_position.y}"
    )


def teleport_mouse():
    """Teleports mouse to the saved coordinates without resetting them."""
    if saved_position is None:
        print_dashboard()
        print("\n[WARNING] No position saved yet! Press the save hotkey first.")
    else:
        pyautogui.moveTo(saved_position.x, saved_position.y)
        print_dashboard()
        print(
            f"\n[SUCCESS] Mouse teleported to X: {saved_position.x}, Y: {saved_position.y}"
        )


def main():
    # Print the terminal menu
    print_dashboard()

    # Register hotkeys
    keyboard.add_hotkey(HOTKEY_SAVE, save_mouse_pos)
    keyboard.add_hotkey(HOTKEY_TELEPORT, teleport_mouse)

    # Keep script running until exit hotkey is pressed
    keyboard.wait(HOTKEY_QUIT)
    print("\nExiting script. Goodbye!")


if __name__ == "__main__":
    main()
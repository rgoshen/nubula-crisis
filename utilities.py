import os

def clear():
    """
    Clears the terminal screen.

    This function clears the terminal screen, using 'cls' for Windows systems
    and 'clear' for Unix-based systems (Linux, macOS). It detects the operating system
    and runs the appropriate command to refresh the display, creating a clean screen for the next output.

    Usage:
        Call this function to clear the terminal screen when needed.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

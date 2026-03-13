import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_console():
    """Clears the terminal screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Wait for user to press Enter."""
    input(f"\n{Style.BRIGHT}Press Enter to return to menu...")

# Simple color constants for easy access
class Colors:
    HEADER = Fore.CYAN + Style.BRIGHT
    MENU = Fore.YELLOW
    SUCCESS = Fore.GREEN
    ERROR = Fore.RED
    INFO = Fore.BLUE
    RESET = Style.RESET_ALL
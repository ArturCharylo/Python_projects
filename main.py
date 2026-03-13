import os
import sys

# Standard library to handle colors (install via: pip install colorama)
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    # Fallback if colorama is not installed
    class Fore: RED = GREEN = YELLOW = CYAN = BLUE = ""
    class Style: BRIGHT = RESET_ALL = ""

# Importing your algorithms from the algorithms folder
try:
    from algorithms.DFS import Graph
    from algorithms.hash_map import HashMap
    from algorithms.binary_search import BinarySearch
    from algorithms.bit_operations import BitwiseOps
    from ui.header import display_header
except ImportError as e:
    print(f"Error: Could not find one of the algorithm modules. {e}")

def clear_console():
    """Clears the terminal screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_console()
        display_header()
        
        print(f"{Fore.CYAN}{Style.BRIGHT}--- Python Projects Menu ---")
        print(f"{Fore.YELLOW}1.{Fore.RESET} Graph Traversal (DFS/BFS)")
        print(f"{Fore.YELLOW}2.{Fore.RESET} Hash Map Demo")
        print(f"{Fore.YELLOW}3.{Fore.RESET} Binary Search & Two Pointers")
        print(f"{Fore.YELLOW}4.{Fore.RESET} Bitwise Operations")
        print(f"{Fore.YELLOW}5.{Fore.RESET} Run Snake Game (Logic)")
        print(f"{Fore.RED}Type 'exit' to quit")
        
        choice = input(f"\n{Fore.GREEN}Enter your choice: {Fore.RESET}").strip().lower()

        if choice == 'exit':
            print(f"{Fore.YELLOW}Goodbye!")
            break

        print("\n" + "="*30) # Separator for better readability
        match choice:
            case '1':
                print(f"{Fore.BLUE}[DFS/BFS Demo]")
                g = Graph()
                g.add_edge(0, 1)
                g.add_edge(0, 2)
                g.add_edge(1, 2)
                print(f"{Fore.GREEN}DFS starting from vertex 0:")
                g.dfs(0)
                print()

            case '2':
                print(f"{Fore.BLUE}[Hash Map Demo]")
                h = HashMap(10)
                h.set_val("test_key", "test_value")
                print(f"{Fore.GREEN}Stored value: {h.get_val('test_key')}")

            case '3':
                print(f"{Fore.BLUE}[Binary Search Demo]")
                bs = BinarySearch(10)
                print(f"{Fore.GREEN}Array: {bs.get_array()}")
                target = bs.get_array()[0]
                print(f"{Fore.GREEN}Searching for {target}: index {bs.bs(target)}")

            case '4':
                print(f"{Fore.BLUE}[Bitwise Ops Demo]")
                ops = BitwiseOps(10, 2)
                print(f"{Fore.GREEN}10 AND 2 = {ops.bit_and()}")

            case '5':
                print(f"{Fore.BLUE}To run the Snake Game, please execute 'python PyGame/snake.py' directly.")

            case _:
                print(f"{Fore.RED}Invalid option. Please enter a number between 1-5 or 'exit'.")
        if choice in ['1', '2', '3', '4', '5']:
            input(f"\n{Style.BRIGHT}Press Enter to return to menu...")

if __name__ == "__main__":
    main_menu()
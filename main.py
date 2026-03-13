import sys
from ui.utils import clear_console, pause, Colors
from ui.header import display_header

# Importing algorithms
try:
    from algorithms.DFS import Graph
    from algorithms.hash_map import HashMap
    from algorithms.binary_search import BinarySearch
    from algorithms.bit_operations import BitwiseOps
except ImportError as e:
    print(f"{Colors.ERROR}Error: Could not find modules. {e}")
    sys.exit(1)

def main_menu():
    while True:
        clear_console()
        display_header()
        
        print(f"{Colors.HEADER}--- Python Projects Menu ---")
        print(f"{Colors.MENU}1.{Colors.RESET} Graph Traversal (DFS/BFS)")
        print(f"{Colors.MENU}2.{Colors.RESET} Hash Map Demo")
        print(f"{Colors.MENU}3.{Colors.RESET} Binary Search & Two Pointers")
        print(f"{Colors.MENU}4.{Colors.RESET} Bitwise Operations")
        print(f"{Colors.MENU}5.{Colors.RESET} Run Snake Game (Logic)")
        print(f"{Colors.ERROR}Type 'exit' to quit")
        
        choice = input(f"\n{Colors.SUCCESS}Enter your choice: {Colors.RESET}").strip().lower()

        if choice == 'exit':
            print(f"{Colors.MENU}Goodbye!")
            break

        print("\n" + "="*30)

        match choice:
            case '1':
                print(f"{Colors.INFO}[DFS/BFS Demo]")
                g = Graph()
                # ... logic ...
                print(f"{Colors.SUCCESS}DFS starting from vertex 0:")
                g.dfs(0)
                print()

            case '2':
                print(f"{Colors.INFO}[Hash Map Demo]")
                h = HashMap(10)
                h.set_val("test_key", "test_value")
                print(f"{Colors.SUCCESS}Stored value: {h.get_val('test_key')}")

            case '3':
                print(f"{Colors.INFO}[Binary Search Demo]")
                bs = BinarySearch(10)
                print(f"{Colors.SUCCESS}Array: {bs.get_array()}")
                target = bs.get_array()[0]
                print(f"{Colors.SUCCESS}Searching for {target}: index {bs.bs(target)}")

            case '4':
                print(f"{Colors.INFO}[Bitwise Ops Demo]")
                ops = BitwiseOps(10, 2)
                print(f"{Colors.SUCCESS}10 AND 2 = {ops.bit_and()}")

            case '5':
                print(f"{Colors.INFO}To run the Snake Game, please execute 'python PyGame/snake.py' directly.")

            case _:
                print(f"{Colors.ERROR}Invalid option.")

        if choice in ['1', '2', '3', '4', '5']:
            pause()

if __name__ == "__main__":
    main_menu()
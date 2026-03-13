import sys
from ui.utils import clear_console, pause, Colors
from ui.header import display_header

# Importing algorithms and game logic
try:
    from algorithms.DFS import Graph
    from algorithms.hash_map import HashMap
    from algorithms.binary_search import BinarySearch
    from algorithms.bit_operations import BitwiseOps
    from PyGame.snake import Game
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
        print(f"{Colors.MENU}5.{Colors.RESET} Run Snake Game")
        print(f"{Colors.ERROR}Type 'exit' to quit")
        
        choice = input(f"\n{Colors.SUCCESS}Enter your choice: {Colors.RESET}").strip().lower()

        if choice == 'exit':
            print(f"{Colors.MENU}Goodbye!")
            break

        match choice:
            case '1':
                clear_console()
                # Full DFS/BFS demonstration with user input
                print(f"{Colors.INFO}[DFS/BFS Demo]")
                g = Graph()
                # Pre-defining a sample graph structure
                g.add_edge(0, 1); g.add_edge(0, 2); g.add_edge(1, 2)
                g.add_edge(2, 0); g.add_edge(2, 3); g.add_edge(3, 3)
                
                try:
                    start_node = int(input("Enter starting vertex (e.g., 2): "))
                    print(f"{Colors.SUCCESS}DFS Traversal:")
                    g.dfs(start_node)
                    print(f"\n{Colors.SUCCESS}BFS Traversal:")
                    g.bfs(start_node)
                    print()
                except ValueError:
                    print(f"{Colors.ERROR}Invalid input. Please enter a number.")

            case '2':
                clear_console()
                # Interactive Hash Map demonstration
                print(f"{Colors.INFO}[Hash Map Demo]")
                size = int(input("Enter hash table size: "))
                h = HashMap(size)
                
                key = input("Enter key to store: ")
                val = input("Enter value for the key: ")
                h.set_val(key, val)
                
                print(f"{Colors.SUCCESS}Current Hash Table: {h}")
                search_key = input("Search for a key: ")
                print(f"{Colors.SUCCESS}Result: {h.get_val(search_key)}")

            case '3':
                clear_console()
                # Binary Search and Two Pointers functionality
                print(f"{Colors.INFO}[Binary Search Demo]")
                length = int(input("Enter array length to generate: "))
                bs = BinarySearch(length)
                print(f"{Colors.SUCCESS}Generated Sorted Array: {bs.get_array()}")
                
                target = int(input("Enter target number to find (Binary Search): "))
                idx = bs.bs(target)
                print(f"{Colors.SUCCESS}Found at index: {idx if idx != -1 else 'Not found'}")
                
                pair_sum = int(input("Enter target sum to check for pairs (Two Pointers): "))
                print(f"{Colors.SUCCESS}Does a pair exist?: {bs.is_pair(pair_sum)}")

            case '4':
                clear_console()
                # Complete Bitwise Operations demonstration
                print(f"{Colors.INFO}[Bitwise Ops Demo]")
                try:
                    a = int(input("Enter first number (a): "))
                    b = int(input("Enter second number (b): "))
                    ops = BitwiseOps(a, b)
                    
                    print(f"{Colors.SUCCESS}AND: {ops.bit_and()} | {ops.to_binary(ops.bit_and())}")
                    print(f"{Colors.SUCCESS}OR:  {ops.bit_or()} | {ops.to_binary(ops.bit_or())}")
                    print(f"{Colors.SUCCESS}XOR: {ops.bit_xor()} | {ops.to_binary(ops.bit_xor())}")
                    print(f"{Colors.SUCCESS}NOT a: {ops.bit_not()} | {ops.to_binary(ops.bit_not())}")
                    print(f"{Colors.SUCCESS}Is 'a' a power of 2?: {ops.is_power_of_2()}")
                except ValueError:
                    print(f"{Colors.ERROR}Please provide valid integers.")

            case '5':
                clear_console()
                # Launching the PyGame Snake instance
                print(f"{Colors.INFO}Launching Snake Game...")
                snake_game = Game(800, 600)
                snake_game.run()

            case _:
                print(f"{Colors.ERROR}Invalid option.")

        if choice in ['1', '2', '3', '4', '5']:
            pause()

if __name__ == "__main__":
    main_menu()
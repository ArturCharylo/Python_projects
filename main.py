# Importing your algorithms from the algorithms folder
try:
    from algorithms.DFS import Graph
    from algorithms.hash_map import HashMap
    from algorithms.binary_search import BinarySearch
    from algorithms.bit_operations import BitwiseOps
    from ui.header import display_header
except ImportError as e:
    print(f"Error: Could not find one of the algorithm modules. {e}")

def main_menu():
    """Main menu to navigate through various Python projects."""

    display_header()

    while True:
        print("\n--- Python Projects Menu ---")
        print("1. Graph Traversal (DFS/BFS)")
        print("2. Hash Map Demo")
        print("3. Binary Search & Two Pointers")
        print("4. Bitwise Operations")
        print("5. Run Snake Game (Logic)")
        print("Type 'exit' to quit")
        
        choice = input("\nEnter your choice: ").strip().lower()

        if choice == 'exit':
            print("Goodbye!")
            break

        match choice:
            case '1':
                print("\n[DFS/BFS Demo]")
                g = Graph()
                g.add_edge(0, 1)
                g.add_edge(0, 2)
                g.add_edge(1, 2)
                print("DFS starting from vertex 0:")
                g.dfs(0)
                print()

            case '2':
                print("\n[Hash Map Demo]")
                h = HashMap(10)
                h.set_val("test_key", "test_value")
                print(f"Stored value: {h.get_val('test_key')}")

            case '3':
                print("\n[Binary Search Demo]")
                bs = BinarySearch(10)
                print(f"Array: {bs.get_array()}")
                target = bs.get_array()[0]
                print(f"Searching for {target}: index {bs.bs(target)}")

            case '4':
                print("\n[Bitwise Ops Demo]")
                ops = BitwiseOps(10, 2)
                print(f"10 AND 2 = {ops.bit_and()}")

            case '5':
                print("\nTo run the Snake Game, please execute 'python PyGame/snake.py' directly.")

            case _:
                print("Invalid option. Please enter a number between 1-5 or 'exit'.")

if __name__ == "__main__":
    main_menu()
from collections import defaultdict, deque
from typing import Any, Set, List

class Graph:
    """A class representing a directed graph using an adjacency list."""

    def __init__(self):
        # Default dictionary to store the graph
        self.graph = defaultdict(list)

    def add_edge(self, u: Any, v: Any) -> None:
        """Adds a directed edge from vertex u to vertex v."""
        self.graph[u].append(v)

    def _dfs_util(self, v: Any, visited: Set[Any]) -> None:
        """Internal helper for recursive DFS traversal."""
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self._dfs_util(neighbour, visited)

    def dfs(self, v: Any) -> None:
        """Performs Depth First Traversal starting from vertex v."""
        visited = set()
        self._dfs_util(v, visited)

    def bfs(self, s: Any) -> None:
        """Performs Breadth First Traversal starting from vertex s."""
        # Using a set for visited nodes makes it work with any hashable type (strings, large ints)
        visited = {s}
        # deque is more efficient than a list for queue operations (O(1) popleft)
        queue = deque([s])

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            for neighbour in self.graph[current_vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Depth First Traversal (starting from vertex 2):")
    g.dfs(2)

    print("\n\nFollowing is Breadth First Traversal (starting from vertex 2):")
    g.bfs(2)
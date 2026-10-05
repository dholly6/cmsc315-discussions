"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Safely handle a starting location that does not exist.
    if start not in graph:
        return []

    visited = []
    visited_set = set()

    # A queue follows FIFO order, allowing BFS to visit
    # nearby nodes before moving farther away.
    queue = deque([start])
    visited_set.add(start)

    while queue:
        current = queue.popleft()
        visited.append(current)

        # Add unvisited neighbors so they can be explored
        # level by level.
        for neighbor in graph[current]:
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)

    # Unlike DFS, BFS explores nearby nodes first instead
    # of following one path as deeply as possible.
    return visited


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")

    # Each node represents a location on a video game map.
    # Each edge represents a path connecting two locations.
    game_map = {
        "Town": ["Forest", "Castle"],
        "Forest": ["Town", "Cave", "River"],
        "Castle": ["Town", "Village"],
        "Cave": ["Forest"],
        "River": ["Forest", "Village"],
        "Village": ["Castle", "River"]
    }

    # Display each location and its connected locations.
    for location, connections in game_map.items():
        print(location, "->", connections)

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    # Begin at Town. BFS visits locations closest to Town first.
    start_location = "Town"

    print("Starting location:", start_location)
    print("BFS traversal:", bfs(game_map, start_location))

    # Add a new location to the game map.
    game_map["Mountain"] = ["Village"]
    game_map["Village"].append("Mountain")

    print("\nAdded new location: Mountain")
    print("Updated BFS traversal:", bfs(game_map, start_location))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Starting from a node that does not exist.
    # BFS safely returns an empty list instead of causing an error.
    print("Missing starting node:", bfs(game_map, "Beach"))

    # Edge case 2: A graph containing only one node.
    # BFS visits the single node and then stops.
    single_location = {
        "Island": []
    }

    print("Single-node graph:", bfs(single_location, "Island"))


if __name__ == "__main__":
    main()

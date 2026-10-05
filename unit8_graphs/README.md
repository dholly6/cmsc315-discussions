# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

While completing this assignment, I learned how graphs can represent connections between different objects and how Breadth-First Search can be used to traverse those connections. I created a video game map using an adjacency list where locations represented nodes and paths represented edges. I also learned how BFS uses a queue to visit nearby nodes level by level.
One challenge was understanding how to prevent BFS from visiting the same node multiple times. I handled this by using a set to keep track of visited nodes before adding new neighbors to the queue. I also tested a missing starting node and a graph containing only one node to see how BFS handled edge cases.
BFS and DFS both traverse graphs, but they explore them differently. BFS visits nearby nodes first using a queue, while DFS follows one path deeper before backtracking. BFS would be useful for finding nearby locations or shortest paths in an unweighted game map. DFS could be useful for exploring deeper paths, such as searching through a maze or discovering connected areas.


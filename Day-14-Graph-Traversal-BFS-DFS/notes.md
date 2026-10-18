# Graph Traversal: BFS & DFS — Notes

## Why traversal?
Traversal visits graph vertices systematically. Track visited vertices: graphs may contain cycles, and without a visited set traversal can repeat forever.

Example adjacency list:
```python
graph = {
    "A": ["B", "C"], "B": ["A", "D", "E"],
    "C": ["A", "F"], "D": ["B"],
    "E": ["B", "F"], "F": ["C", "E"]
}
```

## BFS — Breadth-First Search
BFS explores level by level: start, direct neighbors, then their neighbors. It uses a **queue (FIFO)**. BFS finds shortest paths by number of edges in an **unweighted** graph (or one with equal edge weights). Mark vertices visited when enqueueing them to avoid duplicate queue entries.

## DFS — Depth-First Search
DFS follows a path as far as possible before backtracking. It uses recursion (call stack) or an explicit **stack (LIFO)**. It is useful for reachability, connected components, and cycle-related algorithms. Order depends on neighbor ordering.

## Complexity
With an adjacency list, BFS and DFS take `O(V + E)` time and `O(V)` auxiliary space. `V` = vertices; `E` = edges. With an adjacency matrix, traversal generally takes `O(V²)` because each vertex's full row is scanned.

## BFS shortest path
BFS discovers vertices in nondecreasing number of edges from the start. Store each discovered vertex's parent, then reconstruct a path from target back to source.

## Disconnected graphs
Traversal from one start visits only vertices reachable from that start. To visit every vertex in a disconnected graph, start another traversal at each still-unvisited vertex.

## Common mistakes
- Forgetting `visited`.
- Marking visited too late and queueing duplicates.
- Assuming DFS finds shortest paths.
- Assuming traversal order is unique; it depends on neighbor order.
- Applying unweighted BFS shortest-path logic to arbitrary weighted graphs.

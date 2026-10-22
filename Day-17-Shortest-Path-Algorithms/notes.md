# Notes — Shortest Path Algorithms

## 1. What is a shortest path?
A path from a source vertex to a destination with the fewest edges or the lowest total edge weight.

## 2. BFS — unweighted graphs
BFS explores vertices level by level using a queue. The first time a vertex is reached, its path has the fewest edges.
- Time: `O(V + E)` with an adjacency list.
- Space: `O(V)`.
- Use for unweighted/equal-weight edges.

## 3. Dijkstra — non-negative weighted graphs
Dijkstra repeatedly processes the currently known smallest distance using a min-priority queue (`heapq`). Relax an edge `u -> v` when `dist[u] + weight < dist[v]`.
- Time: typically `O((V + E) log V)` with adjacency lists and a binary heap.
- Space: `O(V + E)` including graph storage.
- All edge weights must be non-negative.

## 4. Path reconstruction
Store `parent[v] = u` whenever a shorter route to `v` is found. Starting at the target, follow parents back to the source and reverse the result.

## 5. Unreachable vertices
Their distance remains infinity (`float('inf')`); the reconstructed path is empty.

## 6. Common mistakes
- Using BFS to optimize total cost when edge weights differ.
- Running Dijkstra on negative-weight edges.
- Forgetting to skip stale heap entries.
- Confusing an unreachable destination with a distance of zero.

## 7. Quick comparison
| Algorithm | Graph | Main idea | Time |
|---|---|---|---|
| BFS | Unweighted/equal weights | Queue, level order | `O(V + E)` |
| Dijkstra | Non-negative weighted | Min-heap, relaxation | `O((V + E) log V)` |

# Graph Fundamentals & Representation — Notes

## 1. Core vocabulary
A graph is written as `G = (V, E)`:
- **Vertex (node):** an entity.
- **Edge:** a connection between vertices.
- **Degree:** number of incident edges in an undirected graph.
- **Path:** a sequence of connected vertices.
- **Cycle:** a path that returns to its starting vertex.
- **Weighted graph:** edges carry values such as cost or distance.

Example undirected graph:
```text
A --- B
|     |
C --- D
```
Edges: A-B, A-C, B-D, C-D.

## 2. Directed vs. undirected
- **Undirected:** `A -- B` represents a connection both ways.
- **Directed:** `A -> B` does not imply `B -> A`.
- **Weighted:** edges can carry values, e.g. `A --(5)-- B`.

For undirected graphs, an edge appears in both endpoints' adjacency lists. For directed graphs, it appears in the source vertex's list.

## 3. Adjacency list
Stores each vertex and its neighbors:
```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}
```
- Space: `O(V + E)`
- Check edge from `u`: typically `O(degree(u))` with lists
- Iterate neighbors of `u`: `O(degree(u))`
- Usually good for sparse graphs.

## 4. Adjacency matrix
A `V x V` table; `matrix[i][j] = 1` means an edge exists. Undirected graph matrices are symmetric.
- Space: `O(V^2)`
- Edge lookup: `O(1)`
- Iterate neighbors of a vertex: `O(V)`
- Useful for dense graphs or frequent edge lookups.

## 5. Weighted adjacency list
Store `(neighbor, weight)` pairs:
```python
weighted = {
    "A": [("B", 5), ("C", 2)],
    "B": [("A", 5)],
    "C": [("A", 2)],
}
```

## 6. Complexity summary
Let `V` be vertices and `E` be edges.

| Operation | Adjacency list | Adjacency matrix |
|---|---:|---:|
| Space | O(V + E) | O(V²) |
| Check edge (u, v) | O(degree(u)) typical | O(1) |
| Iterate neighbors of u | O(degree(u)) | O(V) |
| Add an edge | O(1) amortized | O(1) |

## 7. Common mistakes
- Treating a directed edge as bidirectional.
- Adding an undirected edge to only one endpoint's list.
- Forgetting isolated vertices.
- Confusing vertex count `V` with edge count `E`.
- Assuming matrix space depends on existing edges; it always uses `V²` cells.

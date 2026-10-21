# Notes — Cycle Detection in Graphs

## 1. What is a cycle?
A cycle is a path that starts and ends at the same vertex without repeating intermediate vertices. The exact interpretation depends on whether edges have direction.

- **Undirected:** `0 — 1 — 2 — 0` is a cycle.
- **Directed:** `0 → 1 → 2 → 0` is a cycle because the arrows lead back to the start.
- A directed chain `0 → 1 → 2` is not a cycle.

## 2. Undirected graph: DFS + parent
Track visited vertices. While exploring `node`, ignore the edge back to `parent` because it is the same undirected edge used to enter the node. If another neighbor is already visited, a cycle exists.

```python
if neighbor == parent:
    continue
if visited[neighbor]:
    return True
```

Why parent matters: in an undirected graph, `0 — 1` appears in both adjacency lists. Without ignoring the parent, every normal edge could look like a cycle.

## 3. Directed graph: three DFS states
Use a state array:
- `0` = unvisited
- `1` = currently in the recursion stack (visiting)
- `2` = fully processed (visited/finished)

When exploring an edge `u → v`:
- state `0`: DFS into `v`
- state `1`: back edge; a directed cycle exists
- state `2`: no cycle is implied by this edge alone

A boolean `visited` array alone is insufficient for directed graphs because an edge to a fully processed node is not necessarily a cycle.

## 4. Complexity
With adjacency lists:
- Time: **O(V + E)** because vertices and edges are processed a constant number of times.
- Auxiliary space: **O(V)** for visited/state arrays and the recursion stack.

For a graph with multiple disconnected components, start DFS from every still-unvisited vertex.

## 5. Common mistakes
1. Forgetting to check all components.
2. Treating a directed graph like an undirected graph.
3. In undirected DFS, not ignoring the parent edge.
4. In directed DFS, treating every previously visited neighbor as a cycle instead of checking whether it is still in the recursion stack.
5. Assuming a graph with no cycle must be connected — it can be disconnected and still acyclic.

## 6. Quick checklist
- Is the graph directed or undirected?
- Does the algorithm handle disconnected graphs?
- For undirected DFS, am I tracking the parent?
- For directed DFS, am I distinguishing visiting from finished?

# Notes — Topological Sorting

## What is it?
For every directed edge `u -> v`, `u` must appear before `v` in the ordering. It is used for course prerequisites, build systems, task scheduling, and dependency resolution.

## DFS method
1. Mark a node as visiting (state 1).
2. Visit each neighbor.
3. If a neighbor is visiting, a directed cycle exists.
4. When all neighbors finish, mark the node done (state 2) and append it.
5. Reverse the finishing list.

States: `0 = unvisited`, `1 = currently visiting`, `2 = finished`.

## Kahn's algorithm (BFS / indegree)
1. Compute each vertex's indegree.
2. Queue every vertex with indegree 0.
3. Repeatedly remove a queued vertex, append it, and reduce indegree of its neighbors.
4. If the result contains fewer than `V` vertices, the graph has a cycle.

## Complexity
With an adjacency list, both methods take `O(V + E)` time. Auxiliary space is `O(V)` (excluding graph storage).

## Common mistakes
- Topological sorting applies to directed graphs, and only DAGs have a valid ordering.
- In DFS, a finished node (state 2) is not evidence of a cycle; only an edge to a visiting node (state 1) is.
- Kahn's algorithm must process all vertices to confirm the graph is acyclic.
- Multiple valid orderings may exist. Tests should verify edge order, not one exact list.

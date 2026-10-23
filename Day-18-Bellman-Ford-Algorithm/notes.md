# Notes — Bellman–Ford Algorithm

## What does it solve?
Bellman–Ford finds shortest distances from one source vertex in a weighted directed graph. It supports positive, zero, and negative edge weights. It can also detect a negative-weight cycle reachable from the source.

## Edge relaxation
For an edge `u -> v` with weight `w`, if `dist[u]` is known and `dist[u] + w < dist[v]`, update `dist[v] = dist[u] + w` and record `parent[v] = u`.

## Algorithm
1. Initialize every distance to infinity, except the source at `0`.
2. Repeat `V - 1` times: relax every edge. Stop early if an entire pass makes no changes.
3. Scan all edges one more time. If a reachable edge can still be relaxed, a reachable negative cycle exists.
4. If no such cycle exists, distances are final. Use parent pointers to reconstruct paths.

## Why V - 1 passes?
A shortest simple path can contain at most `V - 1` edges. Each full pass can propagate shortest-path information across another edge.

## Complexity
- Time: `O(V * E)` worst case.
- Extra space: `O(V)` for distances and parents.

## Important details
- Only report a negative cycle if `dist[u]` is finite/reachable before checking `dist[u] + w < dist[v]`.
- A negative cycle that cannot be reached from the chosen source does not affect that source's results.
- For an undirected graph, represent each edge in both directions; a negative undirected edge creates a negative cycle by traversing it back and forth.
- Dijkstra is usually faster, but it does not support negative edge weights.
- Distances for unreachable vertices remain infinity (`float('inf')`).

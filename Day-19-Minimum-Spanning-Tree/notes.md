# Notes — Minimum Spanning Tree

## 1. What is an MST?
A **Minimum Spanning Tree (MST)** is a subset of edges in a connected, undirected, weighted graph that:
- connects every vertex;
- has no cycles;
- has exactly `V - 1` edges;
- has the smallest total edge weight among all spanning trees.

If a graph is disconnected, it has no single spanning tree; an algorithm can instead return a minimum spanning forest.

## 2. Prim's Algorithm
1. Choose any start vertex.
2. Add the cheapest edge that connects a vertex already in the tree to a vertex outside it.
3. Repeat until all vertices are included or no eligible edge remains.

With an adjacency list and min-heap, time is `O(E log V)` (commonly written `O(E log V)` for connected graphs). The implementation uses a heap and a visited set.

## 3. Kruskal's Algorithm
1. Sort all edges by increasing weight.
2. Process edges from lightest to heaviest.
3. Add an edge only if it joins two different components.
4. Use Disjoint Set Union (DSU / Union-Find) to detect whether endpoints are already connected.
5. Stop after `V - 1` edges.

Time: `O(E log E)` dominated by sorting; DSU operations are nearly constant amortized with path compression and union by rank/size.

## 4. Prim vs Kruskal
| Prim | Kruskal |
|---|---|
| Grows one tree from a start vertex | Selects globally lightest safe edges |
| Uses a min-heap / priority queue | Uses sorted edges + DSU |
| Often convenient for dense graphs | Often convenient for sparse graphs |
| Stops when all vertices are reached | Stops after `V - 1` accepted edges |

## 5. Important facts
- MST is for **undirected** weighted graphs.
- Edge weights may be negative; both algorithms can still work.
- Equal weights can lead to multiple valid MSTs.
- A connected graph's MST total weight is unique only if the MST itself is unique; distinct edge weights are a sufficient condition for uniqueness.
- A minimum spanning tree is not the same as a shortest-path tree: MST minimizes total weight of its chosen edges, not each source-to-vertex path.
- If fewer than `V - 1` edges are selected, the graph was disconnected (assuming `V > 0`).

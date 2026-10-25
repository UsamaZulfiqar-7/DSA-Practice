# DSU / Union-Find — Notes

## What is DSU?
Disjoint Set Union maintains a collection of non-overlapping sets. It supports two main operations:
- `find(x)`: identify the representative (root) of the set containing `x`.
- `union(a, b)`: merge the sets containing `a` and `b`; returns `True` if they were separate, otherwise `False`.

## Optimizations
1. **Path compression:** during `find`, make visited nodes point directly to the root.
2. **Union by rank:** attach the shallower tree under the deeper one; increase rank only when ranks are equal.
3. **Union by size:** attach the smaller set under the larger one.

Using path compression plus rank or size gives amortized `O(α(n))` time per operation. `α(n)` is the inverse Ackermann function and is tiny for practical input sizes.

## Example
Initially: `{0}`, `{1}`, `{2}`, `{3}`, `{4}`
- `union(0, 1)` → `{0, 1}`
- `union(1, 2)` → `{0, 1, 2}`
- `union(3, 4)` → `{3, 4}`
- `find(0) == find(2)` → `True`
- `find(0) == find(4)` → `False`

The representative is an implementation detail; do not assume it will always be the smallest element.

## Cycle detection in an undirected graph
Process each edge `(u, v)`:
- If `find(u) == find(v)`, the endpoints are already connected, so this edge closes a cycle.
- Otherwise call `union(u, v)`.

This assumes the graph's edges are processed in a standard undirected-graph cycle-detection setting.

## Complexity
- DSU initialization: `O(n)` time and space.
- `find` / `union`: amortized `O(α(n))` with path compression and rank/size.
- Processing `E` edges after initialization: `O(E α(V))`.

## Common mistakes
- Calling `union` without checking whether both items are already in the same set when cycle detection is needed.
- Forgetting to update the component count after a successful merge.
- Treating DSU as a shortest-path algorithm; it only tracks connectivity/components.
- Using ordinary DSU directly for directed graph cycle detection; the simple method here is for undirected graphs.

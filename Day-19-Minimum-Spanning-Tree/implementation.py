"""Day 19: Prim's and Kruskal's Minimum Spanning Tree algorithms."""
from heapq import heappush, heappop


def prim_mst(graph, start=None):
    """Return (mst_edges, total_weight) using Prim's algorithm.

    graph: {vertex: [(neighbor, weight), ...]} for an undirected graph.
    Returns a minimum spanning tree for a connected graph, or a minimum
    spanning forest for a disconnected graph. Each edge is (u, v, weight).
    """
    if not graph:
        return [], 0
    vertices = list(graph)
    for u, neighbors in graph.items():
        for v, weight in neighbors:
            if v not in graph:
                raise ValueError(f"Neighbor {v!r} is missing from graph keys")
    if start is None:
        start = vertices[0]
    if start not in graph:
        raise ValueError("start vertex must be present in graph")

    visited = set()
    mst_edges = []
    total_weight = 0
    roots = [start] + [v for v in vertices if v != start]

    for root in roots:
        if root in visited:
            continue
        visited.add(root)
        heap = []
        for neighbor, weight in graph[root]:
            heappush(heap, (weight, root, neighbor))
        while heap:
            weight, u, v = heappop(heap)
            if v in visited:
                continue
            visited.add(v)
            mst_edges.append((u, v, weight))
            total_weight += weight
            for neighbor, next_weight in graph[v]:
                if neighbor not in visited:
                    heappush(heap, (next_weight, v, neighbor))
    return mst_edges, total_weight


class DisjointSet:
    """Union-Find with path compression and union by rank."""
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, x):
        if x not in self.parent:
            raise KeyError(f"Unknown vertex: {x!r}")
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        return True


def kruskal_mst(vertices, edges):
    """Return (mst_edges, total_weight) using Kruskal's algorithm.

    vertices: iterable of vertices; edges: iterable of (u, v, weight).
    Returns an MST if connected, otherwise a minimum spanning forest.
    """
    vertices = list(vertices)
    known = set(vertices)
    for u, v, _ in edges:
        if u not in known or v not in known:
            raise ValueError("Every edge endpoint must be in vertices")
    dsu = DisjointSet(vertices)
    mst_edges = []
    total_weight = 0
    for u, v, weight in sorted(edges, key=lambda edge: edge[2]):
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            if len(mst_edges) == max(0, len(vertices) - 1):
                break
    return mst_edges, total_weight


def example_graph():
    """Return the same undirected weighted graph as adjacency list and edges."""
    edges = [
        ("A", "B", 4), ("A", "C", 3), ("B", "C", 1),
        ("B", "D", 2), ("C", "D", 4), ("C", "E", 5),
        ("D", "E", 2),
    ]
    graph = {v: [] for v in "ABCDE"}
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    return graph, edges


if __name__ == "__main__":
    graph, edges = example_graph()
    prim_edges, prim_total = prim_mst(graph, "A")
    kruskal_edges, kruskal_total = kruskal_mst(graph.keys(), edges)
    print("Prim's MST edges:", prim_edges)
    print("Prim's total weight:", prim_total)
    print("Kruskal's MST edges:", kruskal_edges)
    print("Kruskal's total weight:", kruskal_total)

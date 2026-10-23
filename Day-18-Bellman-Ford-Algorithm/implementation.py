"""Bellman–Ford shortest paths with reachable negative-cycle detection."""
from math import inf
from typing import Dict, Hashable, Iterable, List, Tuple, Any

Vertex = Hashable
Edge = Tuple[Vertex, Vertex, float]


def bellman_ford(vertices: Iterable[Vertex], edges: Iterable[Edge], source: Vertex):
    """Return (distances, parents, has_reachable_negative_cycle).

    `edges` contains (u, v, weight) tuples for directed edges.
    Unreachable vertices retain distance infinity. If a reachable negative
    cycle exists, the distance/parent maps are not guaranteed to be final.
    """
    vertex_list = list(vertices)
    edge_list = list(edges)
    if source not in vertex_list:
        raise ValueError("source must be included in vertices")

    dist: Dict[Vertex, float] = {v: inf for v in vertex_list}
    parent: Dict[Vertex, Any] = {v: None for v in vertex_list}
    dist[source] = 0

    for _ in range(max(0, len(vertex_list) - 1)):
        changed = False
        for u, v, weight in edge_list:
            if u not in dist or v not in dist:
                raise ValueError(f"edge endpoint missing from vertices: {(u, v)}")
            if dist[u] != inf and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                changed = True
        if not changed:
            break

    for u, v, weight in edge_list:
        if dist[u] != inf and dist[u] + weight < dist[v]:
            return dist, parent, True

    return dist, parent, False


def reconstruct_path(parent: Dict[Vertex, Any], source: Vertex, target: Vertex):
    """Reconstruct a path from source to target, or return [] if unreachable.

    Call only when Bellman–Ford did not report a reachable negative cycle.
    """
    path = []
    current = target
    seen = set()
    while current is not None:
        if current in seen:
            return []  # defensive guard against invalid/cyclic parent chains
        seen.add(current)
        path.append(current)
        if current == source:
            path.reverse()
            return path
        current = parent.get(current)
    return []


def main():
    vertices = ["A", "B", "C", "D", "E"]
    edges = [
        ("A", "B", 4), ("A", "C", 2), ("C", "B", -1),
        ("B", "D", 2), ("C", "D", 5), ("D", "E", 1),
    ]
    dist, parent, has_cycle = bellman_ford(vertices, edges, "A")
    print("Distances from A:")
    for vertex in vertices:
        print(f"  {vertex}: {dist[vertex]}")
    print("Reachable negative cycle:", has_cycle)
    if not has_cycle:
        print("Path A -> E:", " -> ".join(reconstruct_path(parent, "A", "E")))

    cycle_edges = [("A", "B", 1), ("B", "C", -3), ("C", "A", 1)]
    _, _, cycle_found = bellman_ford(["A", "B", "C"], cycle_edges, "A")
    print("Negative-cycle example detected:", cycle_found)


if __name__ == "__main__":
    main()

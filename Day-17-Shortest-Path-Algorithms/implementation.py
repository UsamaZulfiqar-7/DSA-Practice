"""Day 17: shortest paths with BFS and Dijkstra."""
from collections import deque
from heapq import heappush, heappop
from math import inf


def bfs_shortest_path(graph, source, target):
    """Return (edge_distance, path) for an unweighted adjacency-list graph.

    Returns (inf, []) if target is unreachable. Vertices can be any hashable values.
    """
    if source == target:
        return 0, [source]
    queue = deque([source])
    parent = {source: None}
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                if neighbor == target:
                    path = _reconstruct(parent, target)
                    return len(path) - 1, path
                queue.append(neighbor)
    return inf, []


def dijkstra(graph, source):
    """Return (distances, parents) for weighted graph {u: [(v, weight), ...]}.

    All edge weights must be non-negative. Vertices may be hashable values.
    """
    nodes = set(graph)
    for u, edges in graph.items():
        for v, weight in edges:
            nodes.add(v)
            if weight < 0:
                raise ValueError("Dijkstra requires non-negative edge weights")
    nodes.add(source)
    distances = {node: inf for node in nodes}
    parents = {source: None}
    distances[source] = 0
    heap = [(0, source)]
    while heap:
        current_distance, node = heappop(heap)
        if current_distance != distances[node]:
            continue  # stale heap entry
        for neighbor, weight in graph.get(node, []):
            candidate = current_distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                parents[neighbor] = node
                heappush(heap, (candidate, neighbor))
    return distances, parents


def reconstruct_path(parents, target):
    """Build a path from a Dijkstra parent map; [] means unreachable."""
    if target not in parents:
        return []
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = parents.get(node)
    path.reverse()
    return path


def _reconstruct(parent, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = parent[node]
    return list(reversed(path))


if __name__ == "__main__":
    unweighted = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"], "Z": []}
    distance, path = bfs_shortest_path(unweighted, "A", "E")
    print("BFS shortest path A -> E:", path, "| edges:", distance)

    weighted = {"A": [("B", 4), ("C", 1)], "B": [("D", 1)], "C": [("B", 2), ("D", 5)], "D": [("E", 3)], "E": [], "Z": []}
    distances, parents = dijkstra(weighted, "A")
    print("Dijkstra distances from A:", distances)
    print("Dijkstra shortest path A -> E:", reconstruct_path(parents, "E"))

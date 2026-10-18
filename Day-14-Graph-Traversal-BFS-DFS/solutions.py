"""Reference solutions for selected Day 14 traversal exercises."""
from collections import deque

def bfs_distances(graph, start):
    """Return shortest edge-count distances from start in an unweighted graph."""
    if start not in graph:
        return {}
    distances, queue = {start: 0}, deque([start])
    while queue:
        vertex = queue.popleft()
        for neighbor in graph.get(vertex, []):
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    return distances

def dfs_recursive(graph, start):
    if start not in graph:
        return []
    visited, order = set(), []
    def visit(vertex):
        visited.add(vertex)
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visit(neighbor)
    visit(start)
    return order

def connected_components(graph):
    visited, components = set(), []
    for start in graph:
        if start in visited:
            continue
        component, queue = [], deque([start])
        visited.add(start)
        while queue:
            vertex = queue.popleft()
            component.append(vertex)
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        components.append(component)
    return components

def main():
    graph = {
        "A": ["B", "C"], "B": ["A", "D", "E"],
        "C": ["A", "F"], "D": ["B"], "E": ["B", "F"], "F": ["C", "E"]
    }
    print("BFS distances from A:", bfs_distances(graph, "A"))
    print("Recursive DFS order:", dfs_recursive(graph, "A"))
    disconnected = {"A": ["B"], "B": ["A"], "C": [], "D": ["E"], "E": ["D"]}
    print("Components:", connected_components(disconnected))

if __name__ == "__main__":
    main()

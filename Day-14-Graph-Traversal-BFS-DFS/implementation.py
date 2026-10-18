"""Day 14: BFS and DFS graph traversal."""
from collections import deque

GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

def bfs(graph, start):
    """Return BFS order from start."""
    if start not in graph:
        return []
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)  # Mark when enqueued.
                queue.append(neighbor)
    return order

def dfs_recursive(graph, start):
    """Return recursive DFS order from start."""
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

def dfs_iterative(graph, start):
    """Return iterative DFS order; reverses neighbors to preserve listed order."""
    if start not in graph:
        return []
    visited, stack, order = set(), [start], []
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        order.append(vertex)
        for neighbor in reversed(graph.get(vertex, [])):
            if neighbor not in visited:
                stack.append(neighbor)
    return order

def bfs_shortest_path(graph, start, target):
    """Return a shortest unweighted path as a list, or [] if unreachable."""
    if start not in graph or target not in graph:
        return []
    queue = deque([start])
    parent = {start: None}
    while queue:
        vertex = queue.popleft()
        if vertex == target:
            break
        for neighbor in graph.get(vertex, []):
            if neighbor not in parent:
                parent[neighbor] = vertex
                queue.append(neighbor)
    if target not in parent:
        return []
    path, current = [], target
    while current is not None:
        path.append(current)
        current = parent[current]
    return path[::-1]

def connected_components(graph):
    """Return components for an undirected adjacency-list graph."""
    visited, components = set(), []
    for vertex in graph:
        if vertex in visited:
            continue
        component = []
        queue = deque([vertex])
        visited.add(vertex)
        while queue:
            current = queue.popleft()
            component.append(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        components.append(component)
    return components

def main():
    print("BFS from A:", bfs(GRAPH, "A"))
    print("Recursive DFS from A:", dfs_recursive(GRAPH, "A"))
    print("Iterative DFS from A:", dfs_iterative(GRAPH, "A"))
    print("Shortest path A -> F:", bfs_shortest_path(GRAPH, "A", "F"))
    disconnected = {"A": ["B"], "B": ["A"], "C": [], "D": ["E"], "E": ["D"]}
    print("Connected components:", connected_components(disconnected))

if __name__ == "__main__":
    main()

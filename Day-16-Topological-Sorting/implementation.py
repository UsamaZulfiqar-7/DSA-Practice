"""Topological sorting with DFS and Kahn's algorithm."""
from collections import deque


def _validate_graph(graph):
    vertices = set(graph)
    for neighbors in graph.values():
        vertices.update(neighbors)
    return vertices


def topological_sort_dfs(graph):
    """Return a topological order, or raise ValueError if a cycle exists.

    graph maps each vertex to its list of outgoing neighbors. Vertices that
    occur only as neighbors are supported too.
    """
    vertices = _validate_graph(graph)
    state = {vertex: 0 for vertex in vertices}  # 0 unseen, 1 visiting, 2 done
    order = []

    def dfs(node):
        state[node] = 1
        for neighbor in graph.get(node, []):
            if state[neighbor] == 1:
                raise ValueError("Graph contains a directed cycle")
            if state[neighbor] == 0:
                dfs(neighbor)
        state[node] = 2
        order.append(node)

    for vertex in vertices:
        if state[vertex] == 0:
            dfs(vertex)
    order.reverse()
    return order


def topological_sort_kahn(graph):
    """Return a topological order, or raise ValueError if a cycle exists."""
    vertices = _validate_graph(graph)
    indegree = {vertex: 0 for vertex in vertices}
    for node in vertices:
        for neighbor in graph.get(node, []):
            indegree[neighbor] += 1

    queue = deque(vertex for vertex in vertices if indegree[vertex] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(vertices):
        raise ValueError("Graph contains a directed cycle")
    return order


def is_valid_topological_order(graph, order):
    """Return True if order includes all vertices and respects every edge."""
    vertices = _validate_graph(graph)
    if len(order) != len(vertices) or set(order) != vertices:
        return False
    position = {vertex: i for i, vertex in enumerate(order)}
    return all(position[node] < position[neighbor]
               for node in vertices for neighbor in graph.get(node, []))


if __name__ == "__main__":
    dag = {"A": ["C"], "B": ["C", "D"], "C": ["E"],
           "D": ["F"], "E": ["F"], "F": []}
    for name, algorithm in (("DFS", topological_sort_dfs),
                            ("Kahn", topological_sort_kahn)):
        result = algorithm(dag)
        print(f"{name} order: {result}")
        print("Valid:", is_valid_topological_order(dag, result))

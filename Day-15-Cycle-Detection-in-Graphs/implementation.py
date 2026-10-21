"""Day 15: Cycle detection in directed and undirected graphs."""

from typing import Dict, Hashable, Iterable, List, Set, TypeVar

Node = TypeVar("Node", bound=Hashable)


def has_cycle_undirected(graph: Dict[Node, Iterable[Node]]) -> bool:
    """Return True if an undirected adjacency-list graph contains a cycle.

    The adjacency list should represent an undirected graph (each edge is
    listed for both endpoints). Works with disconnected graphs.
    Time: O(V + E), auxiliary space: O(V).
    """
    visited: Set[Node] = set()

    def dfs(node: Node, parent: Node | None) -> bool:
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor == parent:
                continue
            if neighbor in visited:
                return True
            if dfs(neighbor, node):
                return True
        return False

    for node in graph:
        if node not in visited and dfs(node, None):
            return True
    return False


def has_cycle_directed(graph: Dict[Node, Iterable[Node]]) -> bool:
    """Return True if a directed adjacency-list graph contains a cycle.

    State 0 = unvisited, 1 = visiting/on recursion stack, 2 = finished.
    Works with disconnected graphs.
    Time: O(V + E), auxiliary space: O(V).
    """
    state: Dict[Node, int] = {node: 0 for node in graph}
    # Include neighbors that were not explicitly provided as dictionary keys.
    for neighbors in graph.values():
        for neighbor in neighbors:
            state.setdefault(neighbor, 0)

    def dfs(node: Node) -> bool:
        state[node] = 1
        for neighbor in graph.get(node, []):
            if state[neighbor] == 1:
                return True
            if state[neighbor] == 0 and dfs(neighbor):
                return True
        state[node] = 2
        return False

    for node in state:
        if state[node] == 0 and dfs(node):
            return True
    return False


def build_undirected_graph(edges: Iterable[tuple[Node, Node]]) -> Dict[Node, List[Node]]:
    """Build an undirected adjacency list from edges."""
    graph: Dict[Node, List[Node]] = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    return graph


def build_directed_graph(edges: Iterable[tuple[Node, Node]]) -> Dict[Node, List[Node]]:
    """Build a directed adjacency list from edges."""
    graph: Dict[Node, List[Node]] = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, [])
    return graph


if __name__ == "__main__":
    undirected_cycle = build_undirected_graph([(0, 1), (1, 2), (2, 0), (2, 3)])
    undirected_acyclic = build_undirected_graph([(0, 1), (1, 2), (3, 4)])
    directed_cycle = build_directed_graph([(0, 1), (1, 2), (2, 0), (2, 3)])
    directed_acyclic = build_directed_graph([(0, 1), (0, 2), (1, 3), (2, 3)])

    print("Undirected graph with cycle:", has_cycle_undirected(undirected_cycle))  # True
    print("Undirected graph without cycle:", has_cycle_undirected(undirected_acyclic))  # False
    print("Directed graph with cycle:", has_cycle_directed(directed_cycle))  # True
    print("Directed graph without cycle:", has_cycle_directed(directed_acyclic))  # False

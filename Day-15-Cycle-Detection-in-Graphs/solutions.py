"""Sample answers for selected Day 15 exercises."""

from implementation import (
    build_directed_graph,
    build_undirected_graph,
    has_cycle_directed,
    has_cycle_undirected,
)


def test_examples() -> None:
    # Undirected tree / forest: no cycle.
    forest = build_undirected_graph([(0, 1), (1, 2), (3, 4)])
    assert has_cycle_undirected(forest) is False

    # Undirected triangle: cycle.
    triangle = build_undirected_graph([(0, 1), (1, 2), (2, 0)])
    assert has_cycle_undirected(triangle) is True

    # Directed chain and DAG: no cycle.
    chain = build_directed_graph([(0, 1), (1, 2)])
    assert has_cycle_directed(chain) is False
    dag = build_directed_graph([(0, 1), (0, 2), (1, 3), (2, 3)])
    assert has_cycle_directed(dag) is False

    # Directed cycle.
    directed_cycle = build_directed_graph([(0, 1), (1, 2), (2, 0)])
    assert has_cycle_directed(directed_cycle) is True

    # A self-loop is a cycle in both directed and undirected graph models.
    assert has_cycle_directed(build_directed_graph([(7, 7)])) is True
    assert has_cycle_undirected(build_undirected_graph([(7, 7)])) is True

    print("All sample tests passed!")


def explain_complexity() -> None:
    print("Adjacency-list DFS: O(V + E) time and O(V) auxiliary space.")


if __name__ == "__main__":
    test_examples()
    explain_complexity()

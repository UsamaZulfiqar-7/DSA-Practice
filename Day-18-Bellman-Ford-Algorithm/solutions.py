"""Worked examples and lightweight tests for implementation.py."""
from math import inf
from implementation import bellman_ford, reconstruct_path


def run_tests():
    # Negative edge, but no negative cycle.
    vertices = ["S", "A", "B", "T", "X"]
    edges = [("S", "A", 4), ("S", "B", 5), ("A", "B", -2),
             ("B", "T", 3), ("A", "T", 4)]
    dist, parent, has_cycle = bellman_ford(vertices, edges, "S")
    assert not has_cycle
    assert dist["A"] == 4
    assert dist["B"] == 2
    assert dist["T"] == 5
    assert dist["X"] == inf
    assert reconstruct_path(parent, "S", "T") == ["S", "A", "B", "T"]

    # Reachable negative cycle.
    cycle = [("S", "A", 1), ("A", "B", -2), ("B", "A", -2)]
    _, _, has_cycle = bellman_ford(["S", "A", "B"], cycle, "S")
    assert has_cycle

    # Negative cycle exists, but it is unreachable from S.
    disconnected = [("A", "B", 1), ("S", "T", 2), ("B", "C", -2), ("C", "B", -2)]
    _, _, has_cycle = bellman_ford(["S", "T", "A", "B", "C"], disconnected, "S")
    assert not has_cycle

    # One vertex and no edges.
    dist, _, has_cycle = bellman_ford(["S"], [], "S")
    assert dist["S"] == 0 and not has_cycle

    print("All 4 test groups passed!")


if __name__ == "__main__":
    run_tests()

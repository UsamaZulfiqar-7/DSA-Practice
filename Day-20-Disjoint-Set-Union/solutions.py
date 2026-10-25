"""Sample solutions and tests for Day 20 DSU."""

from implementation import DSU, has_undirected_cycle


def count_components(n: int, edges: list[tuple[int, int]]) -> int:
    dsu = DSU(n)
    for u, v in edges:
        dsu.union(u, v)
    return dsu.components


def count_successful_unions(n: int, pairs: list[tuple[int, int]]) -> int:
    dsu = DSU(n)
    successful = 0
    for a, b in pairs:
        successful += dsu.union(a, b)
    return successful


def run_tests() -> None:
    dsu = DSU(5)
    assert dsu.components == 5
    assert dsu.union(0, 1) is True
    assert dsu.union(1, 2) is True
    assert dsu.union(0, 2) is False
    assert dsu.connected(0, 2)
    assert not dsu.connected(0, 4)
    assert dsu.component_size(1) == 3
    assert dsu.components == 3
    assert count_components(5, [(0, 1), (1, 2), (3, 4)]) == 2
    assert count_successful_unions(3, [(0, 1), (1, 2), (0, 2)]) == 2
    assert has_undirected_cycle(3, [(0, 1), (1, 2), (2, 0)])
    assert not has_undirected_cycle(4, [(0, 1), (1, 2), (2, 3)])
    print("All 6 test groups passed!")


if __name__ == "__main__":
    run_tests()

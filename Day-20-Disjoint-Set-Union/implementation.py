"""Day 20: Disjoint Set Union (Union-Find)."""


class DSU:
    """Disjoint Set Union with path compression and union by size."""

    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n must be non-negative")
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def _check(self, x: int) -> None:
        if not isinstance(x, int) or not 0 <= x < len(self.parent):
            raise IndexError(f"element {x!r} is outside DSU range")

    def find(self, x: int) -> int:
        """Return the root representative, compressing the path."""
        self._check(x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        """Merge two sets. Return True if merged, False if already connected."""
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.components -= 1
        return True

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    def component_size(self, x: int) -> int:
        return self.size[self.find(x)]


def has_undirected_cycle(n: int, edges: list[tuple[int, int]]) -> bool:
    """Return True if an undirected graph contains a cycle."""
    dsu = DSU(n)
    for u, v in edges:
        if not dsu.union(u, v):
            return True
    return False


if __name__ == "__main__":
    dsu = DSU(5)
    print("union(0, 1):", dsu.union(0, 1))
    print("union(1, 2):", dsu.union(1, 2))
    print("union(3, 4):", dsu.union(3, 4))
    print("0 connected to 2:", dsu.connected(0, 2))
    print("0 connected to 4:", dsu.connected(0, 4))
    print("size of component containing 1:", dsu.component_size(1))
    print("components remaining:", dsu.components)
    print("triangle has cycle:", has_undirected_cycle(3, [(0, 1), (1, 2), (2, 0)]))

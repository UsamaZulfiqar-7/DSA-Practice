"""Sample solutions and lightweight tests for Day 17."""
import unittest
from math import inf
from implementation import bfs_shortest_path, dijkstra, reconstruct_path


class ShortestPathTests(unittest.TestCase):
    def test_bfs_path(self):
        graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"]}
        distance, path = bfs_shortest_path(graph, "A", "E")
        self.assertEqual(distance, 3)
        self.assertEqual(path[0], "A")
        self.assertEqual(path[-1], "E")
        self.assertEqual(len(path), 4)

    def test_bfs_same_node(self):
        self.assertEqual(bfs_shortest_path({"A": []}, "A", "A"), (0, ["A"]))

    def test_bfs_unreachable(self):
        distance, path = bfs_shortest_path({"A": ["B"], "B": [], "C": []}, "A", "C")
        self.assertEqual(distance, inf)
        self.assertEqual(path, [])

    def test_dijkstra_and_path(self):
        graph = {"A": [("B", 4), ("C", 1)], "B": [("D", 1)], "C": [("B", 2), ("D", 5)], "D": [("E", 3)], "E": []}
        distances, parents = dijkstra(graph, "A")
        self.assertEqual(distances["E"], 7)
        self.assertEqual(reconstruct_path(parents, "E"), ["A", "C", "B", "D", "E"])

    def test_dijkstra_unreachable(self):
        distances, parents = dijkstra({"A": [], "B": []}, "A")
        self.assertEqual(distances["B"], inf)
        self.assertEqual(reconstruct_path(parents, "B"), [])

    def test_negative_weight_rejected(self):
        with self.assertRaises(ValueError):
            dijkstra({"A": [("B", -1)], "B": []}, "A")


if __name__ == "__main__":
    unittest.main(verbosity=2)

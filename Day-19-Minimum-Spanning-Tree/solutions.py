"""Worked example and lightweight automated tests for Day 19."""
import unittest
from implementation import prim_mst, kruskal_mst, example_graph


class MSTTests(unittest.TestCase):
    def test_prim_and_kruskal_agree(self):
        graph, edges = example_graph()
        prim_edges, prim_total = prim_mst(graph, "A")
        kruskal_edges, kruskal_total = kruskal_mst(graph.keys(), edges)
        self.assertEqual(prim_total, 8)
        self.assertEqual(kruskal_total, 8)
        self.assertEqual(len(prim_edges), 4)
        self.assertEqual(len(kruskal_edges), 4)

    def test_disconnected_graph_returns_forest(self):
        graph = {0: [(1, 2)], 1: [(0, 2)], 2: []}
        edges, total = prim_mst(graph, 0)
        self.assertEqual(len(edges), 1)
        self.assertEqual(total, 2)
        edges2, total2 = kruskal_mst([0, 1, 2], [(0, 1, 2)])
        self.assertEqual(len(edges2), 1)
        self.assertEqual(total2, 2)

    def test_negative_weights_supported(self):
        graph = {"x": [("y", -2)], "y": [("x", -2)]}
        edges, total = prim_mst(graph)
        self.assertEqual(total, -2)
        edges2, total2 = kruskal_mst(["x", "y"], [("x", "y", -2)])
        self.assertEqual(total2, -2)

    def test_empty_graph(self):
        self.assertEqual(prim_mst({}), ([], 0))
        self.assertEqual(kruskal_mst([], []), ([], 0))


if __name__ == "__main__":
    graph, edges = example_graph()
    print("Worked example (A-E):")
    print("Prim:", prim_mst(graph, "A"))
    print("Kruskal:", kruskal_mst(graph.keys(), edges))
    unittest.main(argv=["solutions.py"], exit=False)

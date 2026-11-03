"""Worked examples and lightweight tests for Day 23."""

import unittest
from implementation import (
    coin_change_min,
    house_robber,
    knapsack_01,
    knapsack_01_with_items,
)


class TestClassicDP(unittest.TestCase):
    def test_knapsack(self):
        self.assertEqual(knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7), 9)
        self.assertEqual(knapsack_01([], [], 10), 0)
        self.assertEqual(knapsack_01([2], [10], 1), 0)

    def test_knapsack_reconstruction(self):
        value, indices = knapsack_01_with_items([1, 3, 4, 5], [1, 4, 5, 7], 7)
        self.assertEqual(value, 9)
        self.assertEqual(sum([1, 3, 4, 5][i] for i in indices), 7)
        self.assertEqual(sum([1, 4, 5, 7][i] for i in indices), 9)

    def test_coin_change(self):
        self.assertEqual(coin_change_min([1, 2, 5], 11), 3)
        self.assertEqual(coin_change_min([2], 3), -1)
        self.assertEqual(coin_change_min([1, 3, 4], 0), 0)

    def test_house_robber(self):
        self.assertEqual(house_robber([2, 7, 9, 3, 1]), 12)
        self.assertEqual(house_robber([]), 0)
        self.assertEqual(house_robber([5]), 5)
        self.assertEqual(house_robber([2, 1, 1, 2]), 4)


if __name__ == "__main__":
    print("Worked examples:")
    print("Knapsack:", knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7))
    print("Coin Change:", coin_change_min([1, 2, 5], 11))
    print("House Robber:", house_robber([2, 7, 9, 3, 1]))
    print("\nRunning tests...\n")
    unittest.main(argv=["solutions.py"], verbosity=2)

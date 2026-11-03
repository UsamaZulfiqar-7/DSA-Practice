"""Day 23: implementations of three classic dynamic-programming problems."""

from math import inf
from typing import List, Sequence, Tuple


def knapsack_01(weights: Sequence[int], values: Sequence[int], capacity: int) -> int:
    """Return maximum value; each item can be selected at most once."""
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if capacity < 0 or any(w < 0 for w in weights):
        raise ValueError("capacity and weights must be non-negative")

    dp = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current_capacity in range(capacity, weight - 1, -1):
            dp[current_capacity] = max(
                dp[current_capacity],
                value + dp[current_capacity - weight],
            )
    return dp[capacity]


def knapsack_01_with_items(
    weights: Sequence[int], values: Sequence[int], capacity: int
) -> Tuple[int, List[int]]:
    """Return (maximum value, selected item indices) using a 2D DP table."""
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if capacity < 0 or any(w < 0 for w in weights):
        raise ValueError("capacity and weights must be non-negative")

    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        weight, value = weights[i - 1], values[i - 1]
        for cap in range(capacity + 1):
            dp[i][cap] = dp[i - 1][cap]
            if weight <= cap:
                dp[i][cap] = max(dp[i][cap], value + dp[i - 1][cap - weight])

    selected = []
    cap = capacity
    for i in range(n, 0, -1):
        if dp[i][cap] != dp[i - 1][cap]:
            selected.append(i - 1)
            cap -= weights[i - 1]
    selected.reverse()
    return dp[n][capacity], selected


def coin_change_min(coins: Sequence[int], amount: int) -> int:
    """Return minimum number of unlimited coins, or -1 if impossible."""
    if amount < 0 or any(coin <= 0 for coin in coins):
        raise ValueError("amount must be non-negative and coins must be positive")
    dp = [inf] * (amount + 1)
    dp[0] = 0
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount and dp[current_amount - coin] != inf:
                dp[current_amount] = min(
                    dp[current_amount], dp[current_amount - coin] + 1
                )
    return -1 if dp[amount] == inf else int(dp[amount])


def house_robber(nums: Sequence[int]) -> int:
    """Return the maximum sum with no adjacent elements selected."""
    two_back = 0
    one_back = 0
    for value in nums:
        two_back, one_back = one_back, max(one_back, two_back + value)
    return one_back


if __name__ == "__main__":
    print("0/1 Knapsack:", knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7))
    print("Knapsack with selected indices:", knapsack_01_with_items([1, 3, 4, 5], [1, 4, 5, 7], 7))
    print("Coin Change:", coin_change_min([1, 2, 5], 11))
    print("House Robber:", house_robber([2, 7, 9, 3, 1]))

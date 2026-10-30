"""Day 22: Introductory Dynamic Programming implementations."""
from functools import lru_cache


def fibonacci_memo(n: int) -> int:
    """Return F(n) using top-down memoization. Requires n >= 0."""
    if n < 0:
        raise ValueError("n must be non-negative")

    @lru_cache(maxsize=None)
    def solve(k: int) -> int:
        if k < 2:
            return k
        return solve(k - 1) + solve(k - 2)

    return solve(n)


def fibonacci_tabulation(n: int) -> int:
    """Return F(n) using bottom-up tabulation. O(n) time and space."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fibonacci_optimized(n: int) -> int:
    """Return F(n) using O(1) extra space."""
    if n < 0:
        raise ValueError("n must be non-negative")
    prev2, prev1 = 0, 1
    for _ in range(n):
        prev2, prev1 = prev1, prev2 + prev1
    return prev2


def climbing_stairs_memo(n: int) -> int:
    """Number of ways to climb n stairs taking 1 or 2 steps; n >= 0."""
    if n < 0:
        raise ValueError("n must be non-negative")

    @lru_cache(maxsize=None)
    def ways(k: int) -> int:
        if k <= 1:
            return 1
        return ways(k - 1) + ways(k - 2)

    return ways(n)


def climbing_stairs_tabulation(n: int) -> int:
    """Bottom-up solution to Climbing Stairs; O(n) time and O(1) space."""
    if n < 0:
        raise ValueError("n must be non-negative")
    one_back, two_back = 1, 1
    for _ in range(2, n + 1):
        one_back, two_back = one_back + two_back, one_back
    return one_back


if __name__ == "__main__":
    n = 10
    print(f"Fibonacci F({n}):")
    print("  Memoization:", fibonacci_memo(n))
    print("  Tabulation:", fibonacci_tabulation(n))
    print("  Space optimized:", fibonacci_optimized(n))
    print(f"Ways to climb {n} stairs:", climbing_stairs_tabulation(n))

"""Worked examples and lightweight tests for Day 22."""
from implementation import (
    fibonacci_memo,
    fibonacci_tabulation,
    fibonacci_optimized,
    climbing_stairs_memo,
    climbing_stairs_tabulation,
)


def fibonacci_recursive(n: int) -> int:
    """Simple teaching version; exponential time, so use only for small n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def climbing_stairs_three_steps(n: int) -> int:
    """Number of ways to climb n stairs taking 1, 2, or 3 steps."""
    if n < 0:
        raise ValueError("n must be non-negative")
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if i >= 2:
            dp[i] += dp[i - 2]
        if i >= 3:
            dp[i] += dp[i - 3]
    return dp[n]


def run_tests() -> None:
    for n, expected in [(0, 0), (1, 1), (2, 1), (5, 5), (10, 55), (20, 6765)]:
        assert fibonacci_memo(n) == expected
        assert fibonacci_tabulation(n) == expected
        assert fibonacci_optimized(n) == expected
    for n, expected in [(0, 1), (1, 1), (2, 2), (3, 3), (5, 8), (10, 89)]:
        assert climbing_stairs_memo(n) == expected
        assert climbing_stairs_tabulation(n) == expected
    assert fibonacci_recursive(10) == 55
    assert climbing_stairs_three_steps(4) == 7
    for fn in (fibonacci_memo, fibonacci_tabulation, fibonacci_optimized,
               climbing_stairs_memo, climbing_stairs_tabulation):
        try:
            fn(-1)
        except ValueError:
            pass
        else:
            raise AssertionError(f"{fn.__name__} should reject negative input")
    print("All 4 test groups passed!")


if __name__ == "__main__":
    print("Fibonacci(10):", fibonacci_tabulation(10))
    print("Climbing stairs(5), steps 1 or 2:", climbing_stairs_tabulation(5))
    print("Climbing stairs(4), steps 1, 2, or 3:", climbing_stairs_three_steps(4))
    run_tests()

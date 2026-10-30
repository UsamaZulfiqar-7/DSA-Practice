"""Day 21: Greedy algorithm implementations. Standard library only."""
from typing import Iterable, List, Sequence, Tuple


def activity_selection(activities: Iterable[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Return a maximum-size set of non-overlapping (start, finish) activities.

    An activity is compatible when its start >= the finish of the last selected one.
    Raises ValueError if any activity has start > finish.
    """
    items = list(activities)
    if any(start > finish for start, finish in items):
        raise ValueError("Activity start must be <= finish")
    items.sort(key=lambda activity: (activity[1], activity[0]))
    selected: List[Tuple[int, int]] = []
    last_finish = None
    for start, finish in items:
        if last_finish is None or start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    return selected


def fractional_knapsack(items: Iterable[Tuple[float, float]], capacity: float) -> float:
    """Return maximum value for fractional items given (value, weight).

    Items can be split. All values/weights and capacity must be non-negative;
    item weights must be strictly positive.
    """
    if capacity < 0:
        raise ValueError("Capacity must be non-negative")
    normalized = list(items)
    for value, weight in normalized:
        if value < 0 or weight <= 0:
            raise ValueError("Values must be non-negative and weights positive")
    normalized.sort(key=lambda item: item[0] / item[1], reverse=True)
    total = 0.0
    remaining = float(capacity)
    for value, weight in normalized:
        if remaining <= 0:
            break
        taken = min(float(weight), remaining)
        total += taken * (float(value) / float(weight))
        remaining -= taken
    return total


def greedy_coin_change(amount: int, denominations: Sequence[int]) -> List[int]:
    """Return greedy coin selection for amount; may not be optimal for all systems."""
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    if any(coin <= 0 for coin in denominations):
        raise ValueError("Coin denominations must be positive")
    coins = sorted(set(denominations), reverse=True)
    result: List[int] = []
    remaining = amount
    for coin in coins:
        count, remaining = divmod(remaining, coin)
        result.extend([coin] * count)
    if remaining:
        raise ValueError("Amount cannot be formed with the supplied denominations")
    return result


def main() -> None:
    activities = [(1, 3), (2, 5), (4, 7), (1, 8), (8, 9), (5, 9)]
    print("Activity selection:", activity_selection(activities))
    items = [(60, 10), (100, 20), (120, 30)]
    print("Fractional knapsack value (capacity 50):", fractional_knapsack(items, 50))
    print("Greedy coins for 63 with [25, 10, 5, 1]:", greedy_coin_change(63, [25, 10, 5, 1]))
    print("Note: greedy coin change is not optimal for every denomination system.")


if __name__ == "__main__":
    main()

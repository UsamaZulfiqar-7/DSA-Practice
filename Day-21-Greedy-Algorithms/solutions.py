"""Sample answers and lightweight automated tests for Day 21."""
from implementation import activity_selection, fractional_knapsack, greedy_coin_change


def run_tests() -> None:
    assert activity_selection([(1, 3), (2, 5), (4, 7), (1, 8), (8, 9), (5, 9)]) == [(1, 3), (4, 7), (8, 9)]
    assert activity_selection([(1, 2), (2, 3), (1, 3)]) == [(1, 2), (2, 3)]
    assert abs(fractional_knapsack([(60, 10), (100, 20), (120, 30)], 50) - 240.0) < 1e-9
    assert abs(fractional_knapsack([(30, 5), (40, 10)], 10) - 50.0) < 1e-9
    assert greedy_coin_change(63, [25, 10, 5, 1]) == [25, 25, 10, 1, 1, 1]
    assert greedy_coin_change(6, [1, 3, 4]) == [4, 1, 1]  # greedy, not optimal
    print("All 6 test groups passed!")


def show_sample_answers() -> None:
    print("Q2: Select (1, 2), then (2, 3), for 2 activities.")
    print("Q3: Earliest finish leaves as much remaining time as possible for later activities.")
    print("Q4: O(n log n), dominated by sorting.")
    print("Q6: Take (30,5) fully and 5 units of weight from (40,10): value 50.")
    print("Q7: Items cannot be split in 0/1 knapsack; choosing the highest ratio first can block a better combination.")
    print("Q8: [10, 5, 1, 1, 1].")
    print("Q9: Denominations [1, 3, 4], amount 6: greedy uses 4+1+1; optimal is 3+3.")
    print("Q10: Exchange argument or induction.")
    print("Q11: Reject it, because value/weight ratio is undefined.")


if __name__ == "__main__":
    run_tests()
    show_sample_answers()

"""Day 21 practice questions. Try these before checking solutions.py."""
QUESTIONS = [
    "1. Define a greedy algorithm in your own words.",
    "2. For activities [(1, 2), (2, 3), (1, 3)], find a maximum-size compatible set.",
    "3. Why does sorting activities by finish time help activity selection?",
    "4. What is the time complexity of activity selection when sorting is needed?",
    "5. For fractional knapsack, why sort by value/weight ratio?",
    "6. Find the fractional-knapsack value for items [(30, 5), (40, 10)] and capacity 10.",
    "7. Explain why the fractional-knapsack greedy strategy does not solve 0/1 knapsack in general.",
    "8. Use greedy coin change for amount 18 with denominations [10, 5, 1].",
    "9. Give a counterexample where greedy coin change is not optimal.",
    "10. Name one method used to prove a greedy algorithm correct.",
    "11. What should an implementation do if an item has zero weight in fractional knapsack?",
    "12. Design a greedy strategy for selecting the maximum number of non-overlapping meetings.",
]


def main() -> None:
    for question in QUESTIONS:
        print(question)


if __name__ == "__main__":
    main()

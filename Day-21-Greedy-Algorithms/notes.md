# Day 21 Notes — Greedy Algorithms

## What is a greedy algorithm?
A greedy algorithm builds a solution step by step, choosing what seems best at the current step. It does not normally reconsider earlier choices.

Greedy is useful only when the problem has the right structure. A locally best choice does **not** always lead to a globally optimal solution, so correctness needs a proof or a known greedy property.

## Activity selection
Given activities as `(start, finish)` pairs, choose the maximum number of non-overlapping activities. Sort by finish time, select the first activity, then repeatedly select the next activity whose start is at least the last selected finish.
- Time: `O(n log n)` due to sorting; scan is `O(n)`.
- If input is already sorted by finish time, selection is `O(n)`.

## Fractional knapsack
Each item is `(value, weight)`. Items may be split, so sort by descending value-to-weight ratio and take as much as possible from each item.
- Time: `O(n log n)`.
- This greedy strategy is optimal for **fractional** knapsack, not general 0/1 knapsack.

## Minimum coins
For a coin system such as common denominations `[25, 10, 5, 1]`, repeatedly taking the largest coin not exceeding the remaining amount works. But greedy is not optimal for every coin system. For denominations `[1, 3, 4]` and amount `6`, greedy gives `4 + 1 + 1` (3 coins), while optimal is `3 + 3` (2 coins).

## How to evaluate a greedy idea
1. State the local choice precisely.
2. Check whether choices can be made irrevocably.
3. Try small counterexamples.
4. Prove correctness using an exchange argument, a cut property, or induction.
5. Analyze sorting and traversal costs.

## Common pitfalls
- Assuming every locally optimal strategy is globally optimal.
- Using fractional-knapsack logic for 0/1 knapsack.
- Ignoring interval boundary conventions (this project allows an activity to start exactly when the previous one finishes).
- Forgetting to validate negative weights or invalid item data.

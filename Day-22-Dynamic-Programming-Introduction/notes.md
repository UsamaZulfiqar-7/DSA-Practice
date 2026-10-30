# Dynamic Programming — Notes

## What is DP?
Dynamic Programming (DP) solves a problem by solving smaller subproblems and reusing their results instead of recalculating them.

DP is especially useful when a problem has:
1. **Overlapping subproblems** — the same smaller problem appears repeatedly.
2. **Optimal substructure** — a solution can be built from solutions to smaller subproblems (for optimization problems).

## Two common approaches

### Memoization (Top-Down)
Start with recursion and cache each result. A state is computed only once.

### Tabulation (Bottom-Up)
Start from the smallest states and fill a table iteratively until the target state is reached.

## Fibonacci
`F(0) = 0`, `F(1) = 1`, `F(n) = F(n-1) + F(n-2)`.

- Plain recursive Fibonacci: exponential time, approximately `O(2^n)`.
- Memoized Fibonacci: `O(n)` time and `O(n)` cache/recursion space.
- Tabulated Fibonacci: `O(n)` time and `O(n)` table space.
- Space-optimized Fibonacci: `O(n)` time and `O(1)` extra space.

## Climbing Stairs
For `n` stairs, when you can climb either 1 or 2 stairs at a time:
`ways(n) = ways(n-1) + ways(n-2)`, with `ways(0) = 1` and `ways(1) = 1`.

## How to approach a DP problem
1. Define the state (what does `dp[i]` mean?).
2. Write the transition/recurrence.
3. Set base cases.
4. Choose memoization or tabulation.
5. Return the target state and analyze complexity.

## Common mistakes
- Incorrect base cases.
- Not defining what a DP state represents.
- Updating states in the wrong order.
- Assuming greedy always works when subproblems must be compared.
- Forgetting that a memoized recursive solution uses call-stack space.

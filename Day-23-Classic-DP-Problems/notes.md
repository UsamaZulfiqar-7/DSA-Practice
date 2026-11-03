# Day 23 Notes — Classic DP Problems

## 1. 0/1 Knapsack

There are `n` items. Each item has a weight and value. Choose each item **zero or one time** so total weight does not exceed capacity `W`, while total value is maximized.

Define `dp[i][w]` as the best value using the first `i` items with capacity `w`.

For item `i - 1`:
- Skip it: `dp[i - 1][w]`
- Take it (if it fits): `value[i - 1] + dp[i - 1][w - weight[i - 1]]`

Recurrence:
`dp[i][w] = max(skip, take)` when it fits; otherwise `dp[i][w] = skip`.

Time: `O(nW)`. Table space: `O(nW)`. A 1D optimized version uses `O(W)` space and iterates capacities **backward** so an item is not reused in the same iteration.

## 2. Coin Change — Minimum Coins

Given coin denominations and an amount, find the minimum number of coins needed. Each denomination can be used unlimited times. Return `-1` if impossible.

Let `dp[a]` be the minimum coins needed to make amount `a`.
- `dp[0] = 0`
- Initialize all other states to infinity.
- For each amount `a`, try every coin `c <= a`: `dp[a] = min(dp[a], 1 + dp[a-c])`.

Time: `O(amount * number_of_coins)`. Space: `O(amount)`.

## 3. House Robber

House values are in a row. You cannot rob two adjacent houses. Maximize the total.

For each house, either:
- Skip it: best through previous house.
- Rob it: its value plus best through the house before the previous one.

`dp[i] = max(dp[i-1], nums[i] + dp[i-2])`.

Time: `O(n)`. Space can be optimized to `O(1)` by retaining only the previous two states.

## DP problem-solving checklist
1. Define exactly what each DP state means.
2. Identify the choices at each state.
3. Write the recurrence.
4. Set base cases.
5. Choose a valid iteration order.
6. Return the state representing the requested answer.

## Common mistakes
- Confusing 0/1 Knapsack with unbounded knapsack. For 0/1, process 1D capacities backward.
- Forgetting `dp[0] = 0` in Coin Change.
- Returning `0` for an impossible Coin Change amount instead of `-1`.
- In House Robber, allowing adjacent houses to be selected.
- Not handling empty input or zero capacity.

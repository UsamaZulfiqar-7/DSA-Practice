# Notes — LCS & LIS

## Longest Common Subsequence (LCS)
A subsequence preserves relative order but need not be contiguous. For example, `ACE` is a subsequence of `ABCDE`.

Let `dp[i][j]` be the LCS length of prefixes `a[:i]` and `b[:j]`.
- Base: `dp[0][j] = dp[i][0] = 0`.
- If `a[i-1] == b[j-1]`: `dp[i][j] = 1 + dp[i-1][j-1]`.
- Otherwise: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

Time `O(m*n)`. Length-only space can be optimized to `O(min(m,n))`; reconstruction with a full table uses `O(m*n)` space.

## Longest Increasing Subsequence (LIS)
A strictly increasing subsequence preserves order and each next value is larger; values need not be adjacent. Example: `[2, 3, 7, 18]` is an LIS of `[10, 9, 2, 5, 3, 7, 101, 18]`.

### O(n^2) DP
`dp[i]` = length of the LIS ending at index `i`. Initialize all values to 1. For every `j < i`, if `nums[j] < nums[i]`, update `dp[i] = max(dp[i], dp[j] + 1)`. Answer is `max(dp)` (or 0 for empty input). Time `O(n^2)`, space `O(n)`.

### O(n log n) method
Maintain `tails`, where `tails[k]` is the smallest tail found for an increasing subsequence of length `k+1`. Use binary search (`bisect_left`) to replace the first tail >= current value, or append. Time `O(n log n)`, space `O(n)`. `tails` is not necessarily the actual LIS; predecessor indices are needed for reconstruction.

## LCS vs LIS
| Feature | LCS | LIS |
|---|---|---|
| Input | Two sequences | One sequence |
| Goal | Longest common subsequence | Longest strictly increasing subsequence |
| Typical time | `O(m*n)` | `O(n^2)` or `O(n log n)` |

## Common mistakes
- Subsequence is not substring/subarray: elements need not be adjacent.
- Strict LIS uses `<`, not `<=`.
- Empty input has LIS length 0.
- Do not assume `tails` itself is the final LIS.

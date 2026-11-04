"""Day 24: Longest Common Subsequence and Longest Increasing Subsequence."""
from bisect import bisect_left


def lcs_length(a: str, b: str) -> int:
    """LCS length in O(m*n) time and O(min(m,n)) space."""
    if len(b) > len(a):
        a, b = b, a
    previous = [0] * (len(b) + 1)
    for ca in a:
        current = [0] * (len(b) + 1)
        for j, cb in enumerate(b, 1):
            current[j] = previous[j - 1] + 1 if ca == cb else max(previous[j], current[j - 1])
        previous = current
    return previous[-1]


def lcs_sequence(a: str, b: str) -> str:
    """Reconstruct one LCS in O(m*n) time and space."""
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    out, i, j = [], m, n
    while i and j:
        if a[i - 1] == b[j - 1]:
            out.append(a[i - 1]); i -= 1; j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(out))


def lis_length_dp(nums: list[int]) -> int:
    """Strict LIS length in O(n^2) time and O(n) space."""
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lis_length_fast(nums: list[int]) -> int:
    """Strict LIS length in O(n log n) time and O(n) space."""
    tails = []
    for value in nums:
        pos = bisect_left(tails, value)
        if pos == len(tails):
            tails.append(value)
        else:
            tails[pos] = value
    return len(tails)


def lis_sequence(nums: list[int]) -> list[int]:
    """Reconstruct one strict LIS in O(n log n) time and O(n) space."""
    if not nums:
        return []
    tails, tail_indices = [], []
    previous = [-1] * len(nums)
    for i, value in enumerate(nums):
        pos = bisect_left(tails, value)
        if pos:
            previous[i] = tail_indices[pos - 1]
        if pos == len(tails):
            tails.append(value); tail_indices.append(i)
        else:
            tails[pos] = value; tail_indices[pos] = i
    result, index = [], tail_indices[-1]
    while index != -1:
        result.append(nums[index]); index = previous[index]
    return result[::-1]


if __name__ == "__main__":
    a, b = "ABCBDAB", "BDCABA"
    values = [10, 9, 2, 5, 3, 7, 101, 18]
    print("LCS length:", lcs_length(a, b), "| one LCS:", lcs_sequence(a, b))
    print("LIS O(n^2):", lis_length_dp(values))
    print("LIS O(n log n):", lis_length_fast(values), "| one LIS:", lis_sequence(values))

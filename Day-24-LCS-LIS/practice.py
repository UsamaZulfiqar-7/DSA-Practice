QUESTIONS = [
    "Find the LCS length of 'AGGTAB' and 'GXTXAYB'.",
    "Find one LCS of 'ABCBDAB' and 'BDCABA'.",
    "Explain why LCS is not a substring problem.",
    "Find the LCS length of 'HELLO' and 'YELLOW'.",
    "Find the LIS length of [3, 10, 2, 1, 20].",
    "Find one LIS of [10, 9, 2, 5, 3, 7, 101, 18].",
    "Find strict LIS length of [5, 5, 5, 5].",
    "Compare O(n^2) LIS DP and O(n log n) tails method.",
    "Why does bisect_left support a strictly increasing subsequence?",
    "What should LCS and LIS return for empty input?",
    "Implement LIS reconstruction with predecessor indices.",
    "State the time and space complexity of LCS reconstruction.",
]

if __name__ == "__main__":
    for i, question in enumerate(QUESTIONS, 1):
        print(f"{i:2}. {question}")

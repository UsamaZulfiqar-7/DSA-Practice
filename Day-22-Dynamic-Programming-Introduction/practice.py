"""Day 22 practice exercises. Try solving before checking solutions.py."""
QUESTIONS = [
    "Explain overlapping subproblems in your own words.",
    "Explain optimal substructure and give an example.",
    "Implement Fibonacci using plain recursion.",
    "Implement Fibonacci using memoization.",
    "Implement Fibonacci using bottom-up tabulation.",
    "Optimize tabulated Fibonacci to O(1) extra space.",
    "Define the DP state and recurrence for Climbing Stairs.",
    "Count the ways to climb 5 stairs using 1- or 2-step moves.",
    "Compare memoization and tabulation.",
    "State the time and space complexity of memoized Fibonacci.",
    "Modify Climbing Stairs to allow steps of 1, 2, or 3.",
    "Explain why caching avoids repeated recursive calculations.",
]

if __name__ == "__main__":
    for i, question in enumerate(QUESTIONS, start=1):
        print(f"{i:02d}. {question}")

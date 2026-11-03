"""Day 23 practice set — attempt these before checking solutions.py."""

QUESTIONS = [
    "Implement 0/1 Knapsack using a 2D DP table.",
    "Implement 0/1 Knapsack using O(W) space.",
    "Return the selected item indices in a 0/1 Knapsack solution.",
    "Explain why the 1D 0/1 Knapsack capacity loop runs backward.",
    "Implement minimum Coin Change for unlimited denominations.",
    "Return -1 when a Coin Change amount cannot be formed.",
    "Count the number of ways to make an amount using unlimited coins.",
    "Implement House Robber with O(1) extra space.",
    "Solve House Robber when the input list is empty or has one value.",
    "Reconstruct which houses are robbed in one optimal solution.",
    "Compare 0/1 Knapsack and unbounded Knapsack.",
    "For each problem, define the DP state, recurrence, base case, and complexity.",
]

if __name__ == "__main__":
    for number, question in enumerate(QUESTIONS, start=1):
        print(f"{number:02d}. {question}")

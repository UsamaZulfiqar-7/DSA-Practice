"""Day 15 practice — solve these without looking at solutions.py first."""

EXERCISES = [
    "1. Detect whether an undirected graph contains a cycle using DFS.",
    "2. Explain why an undirected DFS must ignore the parent vertex.",
    "3. Detect whether a directed graph contains a cycle using DFS states.",
    "4. Explain the difference between a visiting node and a finished node.",
    "5. Make both algorithms handle disconnected graphs.",
    "6. Test an undirected tree: it should return False.",
    "7. Test an undirected triangle: it should return True.",
    "8. Test a directed chain 0 -> 1 -> 2: it should return False.",
    "9. Test a directed cycle 0 -> 1 -> 2 -> 0: it should return True.",
    "10. Add a self-loop and decide whether it counts as a cycle.",
    "11. State the time and auxiliary-space complexity for adjacency lists.",
    "12. Challenge: implement cycle detection using BFS (undirected graph).",
]

if __name__ == "__main__":
    print("DAY 15 — CYCLE DETECTION PRACTICE\n")
    for exercise in EXERCISES:
        print(exercise)

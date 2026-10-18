"""Day 14 BFS & DFS exercises. Try first; then check solutions.py."""
def main():
    exercises = [
        "1. Run BFS by hand from A using the graph in implementation.py.",
        "2. Run recursive DFS by hand from A. Record the visit order.",
        "3. Implement BFS using collections.deque.",
        "4. Implement recursive DFS with a visited set.",
        "5. Implement iterative DFS using a list as a stack.",
        "6. Explain why visited is needed when a graph contains cycles.",
        "7. Find the shortest unweighted path from A to F using BFS.",
        "8. Modify BFS to return distance (edge count) to every reachable vertex.",
        "9. Find all connected components of an undirected graph.",
        "10. What changes in complexity if an adjacency matrix is used?",
        "11. Explain why DFS does not guarantee the shortest path.",
        "12. Adapt traversal to a directed graph and explain reachability.",
    ]
    print("DAY 14 — GRAPH TRAVERSAL: BFS & DFS")
    print("\\n".join(exercises))

if __name__ == "__main__":
    main()

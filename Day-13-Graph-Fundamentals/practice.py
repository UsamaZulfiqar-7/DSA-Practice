"""Day 13 Graph Fundamentals practice exercises."""

def main():
    exercises = [
        "1. Define vertex, edge, path, cycle, and degree in your own words.",
        "2. Draw an undirected graph with vertices A, B, C, D and edges A-B, A-C, B-D.",
        "3. Write the adjacency list for the graph from question 2.",
        "4. Write the adjacency matrix for the graph from question 2.",
        "5. Represent A -> B and B -> C as a directed adjacency list. Is C -> B present?",
        "6. Explain why an undirected adjacency matrix is symmetric.",
        "7. Represent a weighted graph with A-B weight 5 and A-C weight 2.",
        "8. Compare memory use for adjacency lists and matrices on a sparse graph.",
        "9. State the edge-lookup complexities for both representations.",
        "10. Add an isolated vertex. How does it appear in each representation?",
        "11. Implement remove_edge() for directed and undirected adjacency-list graphs.",
        "12. Explain the difference between a connected graph and a complete graph.",
    ]
    print("DAY 13 — GRAPH FUNDAMENTALS PRACTICE")
    print("\\n".join(exercises))

if __name__ == "__main__":
    main()

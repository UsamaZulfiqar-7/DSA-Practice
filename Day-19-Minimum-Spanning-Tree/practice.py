"""Day 19 practice exercises. Try these before checking solutions.py."""
QUESTIONS = [
    "Define a spanning tree and a minimum spanning tree.",
    "Why does a tree with V vertices have exactly V - 1 edges?",
    "Implement Prim's algorithm using a min-heap.",
    "Implement Kruskal's algorithm using sorted edges.",
    "What problem does Disjoint Set Union solve in Kruskal's algorithm?",
    "Explain path compression and union by rank.",
    "Find an MST by hand for a small weighted undirected graph.",
    "What should an MST function return if the graph is disconnected?",
    "Can MST algorithms handle negative edge weights? Explain.",
    "Explain why a minimum spanning tree is not necessarily a shortest-path tree.",
    "What happens when several edges share the same weight?",
    "Compare Prim's and Kruskal's time complexities.",
]

if __name__ == "__main__":
    for i, question in enumerate(QUESTIONS, 1):
        print(f"{i}. {question}")

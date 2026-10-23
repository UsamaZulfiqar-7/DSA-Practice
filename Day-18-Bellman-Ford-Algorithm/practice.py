"""Day 18 practice prompts — solve these in your own words/code."""
QUESTIONS = [
    "Implement Bellman–Ford for a directed weighted graph.",
    "Explain what edge relaxation means.",
    "Why are at most V - 1 passes needed?",
    "Detect a negative-weight cycle reachable from the source.",
    "Modify the algorithm to stop early when no distance changes.",
    "Return the shortest path as well as its total cost.",
    "Keep unreachable vertices at infinity and explain why.",
    "Create a graph with a negative edge but no negative cycle.",
    "Create a graph with a negative cycle unreachable from the source.",
    "Explain why the extra pass detects a reachable negative cycle.",
    "Compare Bellman–Ford and Dijkstra in complexity and supported weights.",
    "What happens if a negative cycle is reachable from the source? Can finite shortest distances be defined for affected vertices?",
]

if __name__ == "__main__":
    for i, question in enumerate(QUESTIONS, start=1):
        print(f"{i:02}. {question}")

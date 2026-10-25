"""Day 20 practice exercises. Try these before checking solutions."""

EXERCISES = [
    "Implement find(x) without path compression.",
    "Implement union(a, b) using union by rank.",
    "Explain why union(a, b) can return False.",
    "Count connected components after processing a list of edges.",
    "Determine whether two vertices are connected after a series of unions.",
    "Return the size of the component containing a given vertex.",
    "Detect a cycle in an undirected graph using DSU.",
    "Given n and edges, return the number of components.",
    "Explain the difference between path compression and union by size.",
    "Use DSU to check whether adding one edge creates a cycle.",
    "Discuss why ordinary DSU is not enough for directed cycle detection.",
    "Implement a function that counts successful union operations.",
]

if __name__ == "__main__":
    for i, exercise in enumerate(EXERCISES, start=1):
        print(f"{i:02d}. {exercise}")

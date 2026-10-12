"""Reference examples for Day 13 Graph Fundamentals."""
from implementation import Graph, adjacency_matrix, weighted_adjacency_list


def remove_edge(graph, source, destination):
    """Remove an edge; safely ignore missing edges."""
    if source in graph.adj and destination in graph.adj[source]:
        graph.adj[source].remove(destination)
    if not graph.directed and destination in graph.adj and source in graph.adj[destination]:
        graph.adj[destination].remove(source)


def main():
    directed = Graph(["A", "B"], directed=True)
    directed.add_edge("A", "B")
    print("A -> B:", directed.has_edge("A", "B"))
    print("B -> A:", directed.has_edge("B", "A"))

    undirected = Graph(["A", "B"])
    undirected.add_edge("A", "B")
    print("Before removal:", undirected.adj)
    remove_edge(undirected, "A", "B")
    print("After removal:", undirected.adj)

    print("Matrix:", adjacency_matrix(["A", "B"], [("A", "B")])[1])
    print("Weighted:", weighted_adjacency_list(["A", "B"], [("A", "B", 5)]))

if __name__ == "__main__":
    main()

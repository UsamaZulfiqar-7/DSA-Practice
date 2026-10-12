"""Day 13: Graph representations in Python."""

class Graph:
    """Adjacency-list graph; undirected by default."""
    def __init__(self, vertices=(), directed=False):
        self.directed = directed
        self.adj = {vertex: [] for vertex in vertices}

    def add_vertex(self, vertex):
        self.adj.setdefault(vertex, [])

    def add_edge(self, source, destination):
        self.add_vertex(source)
        self.add_vertex(destination)
        if destination not in self.adj[source]:
            self.adj[source].append(destination)
        if not self.directed and source not in self.adj[destination]:
            self.adj[destination].append(source)

    def has_edge(self, source, destination):
        return source in self.adj and destination in self.adj[source]

    def neighbors(self, vertex):
        return list(self.adj.get(vertex, []))

    def display(self):
        for vertex, neighbors in self.adj.items():
            print(f"{vertex}: {neighbors}")


def adjacency_matrix(vertices, edges, directed=False):
    """Return (ordered_vertices, matrix) for unweighted edges."""
    vertices = list(vertices)
    index = {vertex: i for i, vertex in enumerate(vertices)}
    matrix = [[0 for _ in vertices] for _ in vertices]
    for source, destination in edges:
        if source not in index or destination not in index:
            raise ValueError("Every edge endpoint must be in vertices")
        matrix[index[source]][index[destination]] = 1
        if not directed:
            matrix[index[destination]][index[source]] = 1
    return vertices, matrix


def weighted_adjacency_list(vertices, edges, directed=False):
    """Edges are (source, destination, weight) tuples."""
    graph = {vertex: [] for vertex in vertices}
    for source, destination, weight in edges:
        graph.setdefault(source, []).append((destination, weight))
        graph.setdefault(destination, [])
        if not directed:
            graph[destination].append((source, weight))
    return graph


def main():
    print("UNDIRECTED ADJACENCY LIST")
    graph = Graph(["A", "B", "C", "D"])
    for edge in [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]:
        graph.add_edge(*edge)
    graph.display()
    print("Edge A-D exists?", graph.has_edge("A", "D"))

    print("\nDIRECTED GRAPH")
    directed_graph = Graph(["A", "B", "C"], directed=True)
    directed_graph.add_edge("A", "B")
    directed_graph.add_edge("B", "C")
    directed_graph.display()
    print("A -> B?", directed_graph.has_edge("A", "B"))
    print("B -> A?", directed_graph.has_edge("B", "A"))

    print("\nADJACENCY MATRIX")
    vertices, matrix = adjacency_matrix(["A", "B", "C"], [("A", "B"), ("A", "C")])
    print("Vertices:", vertices)
    for row in matrix:
        print(row)

    print("\nWEIGHTED ADJACENCY LIST")
    print(weighted_adjacency_list(["A", "B", "C"], [("A", "B", 5), ("A", "C", 2)]))

if __name__ == "__main__":
    main()

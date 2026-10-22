"""Example solutions and quick tests for Day 16."""
from implementation import (
    topological_sort_dfs,
    topological_sort_kahn,
    is_valid_topological_order,
)


def run_tests():
    dag = {"A": ["C"], "B": ["C", "D"], "C": ["E"],
           "D": ["F"], "E": ["F"], "F": []}
    for algorithm in (topological_sort_dfs, topological_sort_kahn):
        order = algorithm(dag)
        assert is_valid_topological_order(dag, order)

    assert is_valid_topological_order({}, [])
    assert is_valid_topological_order({1: [], 2: []}, [1, 2])

    cyclic = {1: [2], 2: [3], 3: [1]}
    for algorithm in (topological_sort_dfs, topological_sort_kahn):
        try:
            algorithm(cyclic)
        except ValueError:
            pass
        else:
            raise AssertionError("Expected cycle to raise ValueError")

    print("All tests passed!")


def example_indegree_zero(graph):
    """Solution helper: return vertices with indegree zero."""
    vertices = set(graph)
    for neighbors in graph.values():
        vertices.update(neighbors)
    indegree = {vertex: 0 for vertex in vertices}
    for neighbors in graph.values():
        for neighbor in neighbors:
            indegree[neighbor] += 1
    return [vertex for vertex in vertices if indegree[vertex] == 0]


if __name__ == "__main__":
    run_tests()
    example = {"Study": ["Exam"], "Practice": ["Exam"], "Exam": []}
    print("Initially ready:", example_indegree_zero(example))

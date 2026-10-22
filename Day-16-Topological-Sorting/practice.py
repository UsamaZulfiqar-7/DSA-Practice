"""Day 16 practice prompts. Solve these in your own file."""
QUESTIONS = [
    "Implement topological sorting using DFS.",
    "Implement Kahn's algorithm using indegrees and a queue.",
    "Detect whether a directed graph has a cycle using DFS states.",
    "Detect a cycle by checking whether Kahn processes every vertex.",
    "Return one valid ordering for a course-prerequisite graph.",
    "Explain why topological sorting is impossible for a cyclic graph.",
    "Modify Kahn's algorithm to return False if a cycle exists.",
    "Find all vertices that initially have indegree zero.",
    "Explain why a DAG may have multiple valid topological orders.",
    "Analyze the time and space complexity of both approaches.",
    "Test both algorithms on an empty graph and isolated vertices.",
    "Write a helper that validates a proposed topological ordering.",
]

if __name__ == "__main__":
    for i, question in enumerate(QUESTIONS, 1):
        print(f"{i}. {question}")

# Day 15 — Cycle Detection in Graphs 🔄

Today you will learn to detect cycles in **undirected** and **directed** graphs.

## Learning goals
- Understand what a cycle is in each graph type.
- Detect cycles in an undirected graph with DFS and a parent node.
- Detect cycles in a directed graph with DFS recursion states.
- Know the time and space complexity.

## Files
- `notes.md` — concepts and patterns
- `implementation.py` — reusable implementations and demo
- `practice.py` — exercises (try these before opening solutions)
- `solutions.py` — sample solutions

## Run (from this folder)
```bash
python implementation.py
python practice.py
python solutions.py
```

## Key interview distinction
- **Undirected graph:** when DFS reaches an already-visited neighbor that is **not the parent**, a cycle exists.
- **Directed graph:** a cycle exists when DFS reaches a node that is currently in the recursion stack (a **back edge**). A merely visited node is not enough.

For adjacency-list graphs, both methods run in **O(V + E)** time and use **O(V)** auxiliary space.

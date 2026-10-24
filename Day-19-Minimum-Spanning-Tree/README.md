# Day 19 — Minimum Spanning Tree (Prim's & Kruskal's Algorithms)

This Python learning project explains and implements two classic Minimum Spanning Tree (MST) algorithms for **connected, undirected, weighted graphs**.

## Files
- `notes.md` — core concepts, examples, complexity, and common mistakes
- `implementation.py` — Prim's algorithm and Kruskal's algorithm
- `practice.py` — 12 exercises
- `solutions.py` — worked examples and automated tests

## Run
```bash
python implementation.py
python solutions.py
python practice.py
```

No third-party packages are required. Python 3.9+ recommended.

## Key idea
An MST connects every vertex with the minimum possible total edge weight and contains exactly `V - 1` edges for a connected graph. If the graph is disconnected, the analogous result is a minimum spanning forest.

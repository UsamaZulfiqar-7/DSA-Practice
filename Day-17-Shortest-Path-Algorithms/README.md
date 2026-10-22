# Day 17 — Shortest Path Algorithms

Python implementations of:
- **BFS shortest path** for unweighted graphs (or graphs where every edge has equal cost).
- **Dijkstra's algorithm** for weighted graphs with non-negative edge weights.

## Files
- `notes.md` — concepts, examples, complexity, and common mistakes.
- `implementation.py` — reusable graph and shortest-path implementations.
- `practice.py` — exercises to solve.
- `solutions.py` — sample solutions and tests.

## Run (Python 3.9+)
```powershell
python implementation.py
python solutions.py
python practice.py
```

## Key rule
Do not use Dijkstra when the graph has negative-weight edges. For graphs with negative edges, learn Bellman–Ford next.

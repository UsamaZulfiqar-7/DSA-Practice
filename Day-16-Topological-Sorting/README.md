# Day 16 — Topological Sorting (DFS & Kahn's Algorithm)

Topological sorting orders the vertices of a **directed acyclic graph (DAG)** so every directed edge `u -> v` places `u` before `v`.

## Files
- `notes.md` — concepts and complexity
- `implementation.py` — DFS and Kahn's algorithms
- `practice.py` — practice prompts
- `solutions.py` — example solutions and tests

## Run
```bash
python implementation.py
python solutions.py
python practice.py
```

## Key rule
A topological ordering exists **only if the directed graph has no cycle**. A graph can have more than one valid ordering.

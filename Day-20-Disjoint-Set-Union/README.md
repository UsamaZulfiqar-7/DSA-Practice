# Day 20 — Disjoint Set Union (DSU) / Union-Find

A Python learning project covering the Disjoint Set Union data structure, path compression, union by rank/size, connectivity queries, and cycle detection in undirected graphs.

## Files
- `notes.md` — concepts, examples, complexity, and pitfalls
- `implementation.py` — reusable DSU implementation and demo
- `practice.py` — 12 exercises
- `solutions.py` — sample solutions and tests

## Run
```bash
python implementation.py
python solutions.py
python practice.py
```

## Key complexity
With path compression and union by rank/size, operations take amortized `O(α(n))`, where `α` is the inverse Ackermann function (effectively constant for practical input sizes).

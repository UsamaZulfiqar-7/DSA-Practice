# Day 18 — Bellman–Ford Algorithm

A beginner-friendly Python project for learning the Bellman–Ford shortest-path algorithm, including negative edge weights and negative-cycle detection.

## Files
- `notes.md` — core concepts, algorithm steps, complexity, and common mistakes
- `implementation.py` — reusable Bellman–Ford implementation and runnable examples
- `practice.py` — 12 practice prompts
- `solutions.py` — worked examples and basic automated checks

## Run
```bash
python implementation.py
python solutions.py
python practice.py
```

## Key idea
Relax every edge up to `V - 1` times. Then make one additional pass: if any reachable edge can still be relaxed, a reachable negative-weight cycle exists.

Time complexity: `O(V * E)`; auxiliary space: `O(V)` (excluding graph input).

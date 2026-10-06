# Day 8 — Queue

Queue is a linear data structure following **FIFO (First In, First Out)**.

## Core Operations
- Enqueue: add at rear — O(1) with `deque`
- Dequeue: remove from front — O(1) with `deque`
- Front/Peek: view first item — O(1)
- Is Empty — O(1)

## Python
```python
from collections import deque
q = deque()
q.append(10)       # enqueue
q.popleft()        # dequeue
q[0]               # front
```

Avoid `list.pop(0)` for large queues because it is O(n).

## Types
- Simple Queue
- Circular Queue
- Deque
- Priority Queue

## Applications
- Scheduling
- Printer/customer queues
- BFS graph traversal
- Tree level-order traversal
- Buffers and streaming

## Files
- `notes.md` — concepts
- `implementation.py` — implementations
- `practice.py` — 10 questions
- `solutions.py` — solutions

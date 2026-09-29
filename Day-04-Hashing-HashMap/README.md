# Day 4 — Hashing / HashMap

Hashing is a technique used to store and retrieve data efficiently using **key-value pairs**.

In Python, the main HashMap implementation is the built-in **dictionary (`dict`)**.

## Learning Goals

- Understand hashing and HashMap
- Understand key-value pairs
- Learn Python `dict`
- Insert, update, delete, and search data
- Count frequencies using HashMap
- Find duplicates
- Solve common DSA problems using HashMap
- Understand average time complexity

## Why Hashing?

A normal list may require scanning many elements to find a value. A HashMap lets us usually access a value by its key in **O(1) average time**.

Example:

```python
student = {
    "name": "Usama",
    "age": 22,
    "cgpa": 3.85
}

print(student["name"])
```

Output:

```text
Usama
```

## Main Operations

| Operation | Average Time |
|---|---:|
| Insert | O(1) |
| Search | O(1) |
| Update | O(1) |
| Delete | O(1) |

> Worst-case performance can be O(n), but O(1) average time is the usual complexity used for HashMap operations.

## Topics Covered

1. Hashing basics
2. HashMap / Dictionary
3. Insert and update
4. Search and membership
5. Delete
6. Frequency counting
7. Duplicate detection
8. Two Sum
9. Character frequency
10. Grouping/counting with HashMap

## Files

- `notes.md` — theory and concepts
- `implementation.py` — practical Python implementations
- `practice.py` — practice questions

## Practice Goal

Try to solve each problem yourself before checking any solution. Focus on recognizing when a HashMap can reduce a problem from O(n²) to O(n).

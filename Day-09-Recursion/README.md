# Day 9 — Recursion

Recursion is a technique where a function calls itself to solve a smaller version of the same problem.

## Two Essential Parts
1. **Base Case** — stops recursion.
2. **Recursive Case** — calls the function with a smaller/simpler input.

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
```

## Core Topics
- Base case and recursive case
- Call stack
- Factorial
- Sum of numbers
- Fibonacci
- Power
- String reversal
- Palindrome
- Recursive array sum
- Recursive binary search
- GCD
- Backtracking introduction

## Complexity
Simple one-call recursion often uses O(n) auxiliary call-stack space. Fibonacci's naive recursive version takes exponential time.

## Files
- `notes.md` — concepts
- `implementation.py` — examples
- `practice.py` — 10 questions
- `solutions.py` — solutions

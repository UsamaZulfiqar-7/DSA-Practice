# Recursion Notes

## Base Case
The base case stops recursive calls.

```python
if n == 0:
    return
```

## Recursive Case
The recursive call must move toward the base case.

```python
return n * factorial(n - 1)
```

## Factorial
`n! = n × (n-1)!`, with `0! = 1`.

Time O(n), stack space O(n).

## Fibonacci
`F(0)=0`, `F(1)=1`, `F(n)=F(n-1)+F(n-2)`.
Naive recursion is approximately O(2^n) because it repeats subproblems.

## Call Stack
Each recursive call creates a stack frame. Calls return in reverse order, connecting recursion to the Stack data structure.

## Recursive Binary Search
Each call discards half the search space. Time O(log n), auxiliary stack O(log n).

## Recursion vs Iteration
Recursion can be elegant for trees and backtracking but uses call-stack memory and can hit recursion-depth limits. Loops often have lower overhead for simple repetition.

## Backtracking
Choose → explore → undo → try another choice. Used for subsets, permutations, N-Queens, maze solving, and combination problems.

## Questions to Ask
1. What is the base case?
2. How does the input become smaller?
3. What should the function return?
4. How are recursive results combined?

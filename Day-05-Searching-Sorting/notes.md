# Day 5 Notes — Searching & Sorting

## 1. Searching
Searching means finding a target value in a collection.

### Linear Search
Check elements one by one from left to right.
- Works on sorted and unsorted data
- Time: O(n)
- Space: O(1)

### Binary Search
Repeatedly checks the middle element and removes half of the search space.
- Requires sorted data
- Time: O(log n)
- Space: O(1) for iterative implementation

Example: `[10, 20, 30, 40, 50]`, target `40`
1. Middle = 30
2. 40 is larger, search right half
3. Middle of remaining part = 40 → found

## 2. Sorting
Sorting arranges data in an order such as ascending or descending.

### Bubble Sort
Compare adjacent elements and swap them when they are in the wrong order. Large elements gradually move to the end.

### Selection Sort
Find the smallest element from the unsorted part and place it at the current position.

### Insertion Sort
Build the sorted part one element at a time by inserting each new element into its correct position.

## Complexity Comparison
| Algorithm | Best | Average | Worst | Extra Space |
|---|---:|---:|---:|---:|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) iterative |
| Bubble Sort | O(n) optimized | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |

## Important Interview Points
- Binary Search is much faster than Linear Search for large sorted data.
- Do not use Binary Search on an unsorted list without first establishing the required ordering.
- Python's built-in `sort()` / `sorted()` are preferred in real applications, but manual sorting algorithms are important for DSA learning.

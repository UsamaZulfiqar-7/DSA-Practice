# Heap & Priority Queue — Notes

## 1. Heap property
A binary heap is a **complete binary tree**: levels are filled left to right, except possibly the last level.
- Min-heap: parent <= children.
- Max-heap: parent >= children.
Only the root is guaranteed to be the minimum/maximum; the other elements are not fully sorted.

## 2. Python `heapq`
```python
import heapq
heap = []
heapq.heappush(heap, 7)
heapq.heappush(heap, 2)
heapq.heappush(heap, 5)
smallest = heapq.heappop(heap)  # 2
```
For a max-heap of numbers, store negative values and negate the popped result.

## 3. Array index relationships (0-based)
- Parent: `(i - 1) // 2`
- Left child: `2 * i + 1`
- Right child: `2 * i + 2`

## 4. Priority queue
A priority queue removes items by priority rather than insertion order. In this package, smaller numeric priority is served first. Use `(priority, sequence, item)` tuples to preserve insertion order for ties and avoid comparing arbitrary payload objects.

## 5. Complexity
| Operation | Time |
|---|---:|
| Peek root | O(1) |
| Push / insert | O(log n) |
| Pop root | O(log n) |
| Build heap with `heapify` | O(n) |
| Search arbitrary item | O(n) |
| Pop all items in sorted order | O(n log n) |

## 6. Common patterns
- Kth largest/smallest element
- Top K frequent values
- Merge K sorted lists
- Scheduling tasks by priority
- Running median using two heaps

## 7. Common mistakes
- Assuming the entire heap is sorted.
- Forgetting Python `heapq` is a min-heap.
- Using tuples without a tie-breaker when payload objects are not comparable.
- Confusing heaps with BSTs: heaps optimize access to the root, not arbitrary search.

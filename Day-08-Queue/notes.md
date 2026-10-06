# Queue Notes

## FIFO
First In, First Out — like a normal line of people.

## Enqueue
Adds at the rear. With `collections.deque`: O(1).

## Dequeue
Removes from the front. With `deque.popleft()`: O(1).

## Front / Peek
Returns the first element without removing it.

## Queue vs Stack
| Queue | Stack |
|---|---|
| FIFO | LIFO |
| Insert rear | Insert top |
| Remove front | Remove top |
| BFS | DFS/backtracking |

## Circular Queue
Reuses storage by wrapping the rear/front indexes around with modulo arithmetic.

## Deque
Double-ended queue. Supports insertion/removal from both ends.

## BFS
Breadth-First Search uses a queue: dequeue a node, visit it, then enqueue unvisited neighbors.

## Complexity
Using `deque`: enqueue O(1), dequeue O(1), front O(1), space O(n).

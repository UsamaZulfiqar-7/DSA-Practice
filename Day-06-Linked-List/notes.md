# Linked List Notes

## What is a Linked List?
A linked list is a collection of nodes connected through references. Nodes do not need contiguous memory locations.

## Node
A node normally contains `data` and `next`.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Head
`head` points to the first node.

```text
head -> 10 -> 20 -> 30 -> None
```

## Traversal
Start at head and follow `next` until `None`. Time: O(n).

## Insert at Beginning
Point the new node to the current head, then make it the new head. Time: O(1).

## Insert at End
Traverse to the last node and attach the new node. Time: O(n) without a tail pointer.

## Delete
Connect the previous node to the node after the target.

```text
10 -> 20 -> 30
Delete 20
10 ------> 30
```

## Search
Check nodes one by one. Time: O(n).

## Reverse
Use `previous`, `current`, and `next_node`. Time: O(n), extra space O(1).

## Slow/Fast Pointers
Use a slow pointer moving one step and a fast pointer moving two steps. This is useful for finding the middle and detecting cycles.

## Linked List vs Python List
| Feature | Python List | Linked List |
|---|---|---|
| Random access | O(1) | O(n) |
| Insert beginning | O(n) | O(1) |
| Search | O(n) | O(n) |
| Extra references | No | Yes |

## Important Terms
Node, Head, Tail, Next, Traversal, Singly Linked List, Doubly Linked List, Circular Linked List.

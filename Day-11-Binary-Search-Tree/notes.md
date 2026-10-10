# Binary Search Tree (BST) Notes

## 1. BST property
For every node, all values in its left subtree are smaller and all values in its right subtree are greater. Both subtrees must also follow the same rule.

Example:
```text
        50
       /  \\
     30    70
    / \\    / \\
   20 40  60 80
```

Inorder traversal (Left, Node, Right) returns sorted values: `20, 30, 40, 50, 60, 70, 80`.

## 2. Operations
- **Search:** compare target with current node and move left or right.
- **Insert:** follow comparisons until an empty child position is found.
- **Minimum:** keep moving left.
- **Maximum:** keep moving right.
- **Delete:** three cases:
  1. Leaf: remove it.
  2. One child: replace it with its child.
  3. Two children: copy the inorder successor (smallest value in right subtree), then delete that successor.

## 3. Validate a BST
Checking only `left < node < right` for immediate children is insufficient. Every node must respect bounds inherited from all ancestors.

## 4. Successor and predecessor
- Inorder successor is the next larger value. If a node has a right subtree, it is the minimum of that subtree.
- Inorder predecessor is the next smaller value. If a node has a left subtree, it is the maximum of that subtree.

## 5. Complexity
Let `h` be tree height.

| Operation | Time |
|---|---:|
| Search / Insert / Delete | O(h) |
| Minimum / Maximum | O(h) |
| Validate BST | O(n) |
| Inorder traversal | O(n) |

Balanced BST: `h ≈ log n`, so search/insert/delete are `O(log n)`.
Skewed BST: `h ≈ n`, so these operations can become `O(n)`.
A normal BST does not rebalance itself automatically. AVL and Red-Black trees are self-balancing variants.

## 6. Common mistakes
- Checking only immediate children while validating.
- Forgetting to reconnect a parent after deletion.
- Mishandling the two-child deletion case.
- Assuming BST operations are always `O(log n)`.
- Not defining duplicate behavior.

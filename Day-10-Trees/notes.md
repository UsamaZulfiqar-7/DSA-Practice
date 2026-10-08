# Trees Notes

## Binary Tree
Each node has at most two children: left and right.

```text
        10
       /  \\
      5    15
     / \\
    2   7
```

## Terms
- Root: top node
- Parent: node with children
- Child: node below a parent
- Leaf: node with no children
- Height: longest downward path to a leaf
- Depth: distance from root

## DFS
Preorder = Root, Left, Right
Inorder = Left, Root, Right
Postorder = Left, Right, Root

## BFS
Level-order visits nodes level by level and uses a queue.

## BST
For each node:
`left < root < right`

Inorder traversal of a valid BST produces sorted values.

## Recursion
Trees are naturally recursive because each child is itself the root of a subtree.

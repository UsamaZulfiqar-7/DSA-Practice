"""Day 11: BST implementation. Duplicate integer values are ignored."""
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class TreeNode:
    value: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

class BST:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = TreeNode(value)
            return
        current = self.root
        while True:
            if value == current.value:
                return
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right

    def search(self, value: int) -> bool:
        current = self.root
        while current:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def minimum(self, node: Optional[TreeNode] = None) -> Optional[int]:
        current = self.root if node is None else node
        if current is None:
            return None
        while current.left:
            current = current.left
        return current.value

    def maximum(self, node: Optional[TreeNode] = None) -> Optional[int]:
        current = self.root if node is None else node
        if current is None:
            return None
        while current.right:
            current = current.right
        return current.value

    def delete(self, value: int) -> None:
        self.root = self._delete(self.root, value)

    def _delete(self, node: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:       # leaf or only right child
                return node.right
            if node.right is None:      # only left child
                return node.left
            successor = node.right      # two children: inorder successor
            while successor.left:
                successor = successor.left
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
        return node

    def inorder(self) -> List[int]:
        result = []
        def walk(node):
            if node is None:
                return
            walk(node.left)
            result.append(node.value)
            walk(node.right)
        walk(self.root)
        return result

    def is_valid(self) -> bool:
        def validate(node, low, high):
            if node is None:
                return True
            if low is not None and node.value <= low:
                return False
            if high is not None and node.value >= high:
                return False
            return validate(node.left, low, node.value) and validate(node.right, node.value, high)
        return validate(self.root, None, None)

def main():
    tree = BST()
    for value in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(value)
    print("Inorder:", tree.inorder())
    print("Search 40:", tree.search(40))
    print("Search 99:", tree.search(99))
    print("Minimum:", tree.minimum())
    print("Maximum:", tree.maximum())
    print("Valid BST:", tree.is_valid())
    tree.delete(20)
    tree.delete(30)
    tree.delete(50)
    print("After deletions:", tree.inorder())

if __name__ == "__main__":
    main()

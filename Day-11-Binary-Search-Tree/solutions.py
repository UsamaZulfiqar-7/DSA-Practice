"""Reference solutions and demonstrations for Day 11."""
from implementation import BST, TreeNode

def is_valid_bst(root):
    def check(node, low, high):
        if node is None:
            return True
        if low is not None and node.value <= low:
            return False
        if high is not None and node.value >= high:
            return False
        return check(node.left, low, node.value) and check(node.right, node.value, high)
    return check(root, None, None)

def inorder_successor(node):
    if node is None or node.right is None:
        return None
    current = node.right
    while current.left:
        current = current.left
    return current

def main():
    tree = BST()
    for value in [45, 25, 65, 15, 35, 55, 75]:
        tree.insert(value)
    print("Sorted inorder:", tree.inorder())
    print("Valid BST:", is_valid_bst(tree.root))
    tree.delete(15)  # leaf
    tree.delete(25)  # one child after 15 is removed
    tree.delete(45)  # two children
    print("After deleting 15, 25, 45:", tree.inorder())

if __name__ == "__main__":
    main()

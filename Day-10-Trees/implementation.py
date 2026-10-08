from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root is None: return []
    return [root.data] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if root is None: return []
    return inorder(root.left) + [root.data] + inorder(root.right)

def postorder(root):
    if root is None: return []
    return postorder(root.left) + postorder(root.right) + [root.data]

def level_order(root):
    if root is None: return []
    q, result = deque([root]), []
    while q:
        node = q.popleft(); result.append(node.data)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return result

def count_nodes(root):
    if root is None: return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def height(root):
    if root is None: return -1
    return 1 + max(height(root.left), height(root.right))

def search(root, target):
    if root is None: return False
    if root.data == target: return True
    return search(root.left, target) or search(root.right, target)

class BST:
    def __init__(self): self.root = None
    def insert(self, value): self.root = self._insert(self.root, value)
    def _insert(self, node, value):
        if node is None: return TreeNode(value)
        if value < node.data: node.left = self._insert(node.left, value)
        elif value > node.data: node.right = self._insert(node.right, value)
        return node
    def search(self, value):
        cur = self.root
        while cur:
            if value == cur.data: return True
            cur = cur.left if value < cur.data else cur.right
        return False

if __name__ == '__main__':
    root = TreeNode(10); root.left = TreeNode(5); root.right = TreeNode(15)
    root.left.left = TreeNode(2); root.left.right = TreeNode(7); root.right.right = TreeNode(20)
    print('Preorder:', preorder(root)); print('Inorder:', inorder(root)); print('Postorder:', postorder(root))
    print('Level order:', level_order(root)); print('Count:', count_nodes(root)); print('Height:', height(root))
    print('Search 7:', search(root, 7))
    bst = BST()
    for x in [8,3,10,1,6,14,4,7,13]: bst.insert(x)
    print('BST inorder:', inorder(bst.root)); print('BST search 7:', bst.search(7))

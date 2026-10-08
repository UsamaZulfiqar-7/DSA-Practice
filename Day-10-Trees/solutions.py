from collections import deque
class TreeNode:
    def __init__(self,data): self.data=data; self.left=None; self.right=None

def preorder(r): return [] if r is None else [r.data]+preorder(r.left)+preorder(r.right)
def inorder(r): return [] if r is None else inorder(r.left)+[r.data]+inorder(r.right)
def postorder(r): return [] if r is None else postorder(r.left)+postorder(r.right)+[r.data]
def count_nodes(r): return 0 if r is None else 1+count_nodes(r.left)+count_nodes(r.right)
def height(r): return -1 if r is None else 1+max(height(r.left),height(r.right))
def level_order(r):
    if r is None:return []
    q=deque([r]); out=[]
    while q:
        n=q.popleft(); out.append(n.data)
        if n.left:q.append(n.left)
        if n.right:q.append(n.right)
    return out
def search(r,x):
    if r is None:return False
    return r.data==x or search(r.left,x) or search(r.right,x)
def is_valid_bst(r):
    def ok(n,lo,hi):
        if n is None:return True
        if not lo<n.data<hi:return False
        return ok(n.left,lo,n.data) and ok(n.right,n.data,hi)
    return ok(r,float('-inf'),float('inf'))
def find_min_bst(r):
    if r is None:return None
    while r.left:r=r.left
    return r.data

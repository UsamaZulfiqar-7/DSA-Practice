from collections import deque

class Queue:
    def __init__(self): self.items=deque()
    def enqueue(self,x): self.items.append(x)
    def dequeue(self): return self.items.popleft() if self.items else None
    def front(self): return self.items[0] if self.items else None
    def rear(self): return self.items[-1] if self.items else None
    def is_empty(self): return not self.items
    def size(self): return len(self.items)

def simulate():
    q=deque([10,20,30]); q.popleft(); q.append(40); return list(q)

def get_front_rear(q): return (q[0],q[-1]) if q else (None,None)

def reverse_queue(q):
    stack=[]
    while q: stack.append(q.popleft())
    while stack: q.append(stack.pop())
    return q

def generate_binary_numbers(n):
    result=[]; q=deque(["1"])
    for _ in range(n):
        x=q.popleft(); result.append(x); q.append(x+'0'); q.append(x+'1')
    return result

class CircularQueue:
    def __init__(self, capacity):
        self.capacity=capacity; self.data=[None]*capacity; self.front_index=0; self.rear_index=0; self.count=0
    def enqueue(self,x):
        if self.count==self.capacity: return False
        self.data[self.rear_index]=x; self.rear_index=(self.rear_index+1)%self.capacity; self.count+=1; return True
    def dequeue(self):
        if not self.count: return None
        x=self.data[self.front_index]; self.data[self.front_index]=None; self.front_index=(self.front_index+1)%self.capacity; self.count-=1; return x
    def front(self): return self.data[self.front_index] if self.count else None
    def is_empty(self): return self.count==0
    def is_full(self): return self.count==self.capacity

def first_non_repeating(stream):
    freq={}; q=deque(); result=[]
    for c in stream:
        freq[c]=freq.get(c,0)+1; q.append(c)
        while q and freq[q[0]]>1: q.popleft()
        result.append(q[0] if q else '#')
    return result

def generate_5_6(n):
    result=[]; q=deque(['5','6'])
    for _ in range(n):
        x=q.popleft(); result.append(x); q.append(x+'5'); q.append(x+'6')
    return result

def sliding_window_maximum(arr,k):
    if k<=0 or k>len(arr): return []
    q=deque(); result=[]
    for i,x in enumerate(arr):
        while q and q[0] <= i-k: q.popleft()
        while q and arr[q[-1]] <= x: q.pop()
        q.append(i)
        if i>=k-1: result.append(arr[q[0]])
    return result

def bfs(graph,start):
    visited={start}; q=deque([start]); result=[]
    while q:
        node=q.popleft(); result.append(node)
        for nxt in graph.get(node,[]):
            if nxt not in visited: visited.add(nxt); q.append(nxt)
    return result

if __name__=='__main__':
    print(simulate())
    print(list(reverse_queue(deque([1,2,3,4,5]))))
    print(generate_binary_numbers(5))
    print(first_non_repeating('aabc'))
    print(generate_5_6(6))
    print(sliding_window_maximum([1,3,-1,-3,5,3,6,7],3))
    print(bfs({0:[1,2],1:[3],2:[4],3:[],4:[]},0))

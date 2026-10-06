from collections import deque

class Queue:
    def __init__(self): self.items = deque()
    def enqueue(self, value): self.items.append(value)
    def dequeue(self): return self.items.popleft() if self.items else None
    def front(self): return self.items[0] if self.items else None
    def is_empty(self): return not self.items
    def size(self): return len(self.items)
    def display(self): print("Front ->", list(self.items), "<- Rear")

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front_index = self.rear_index = self.count = 0
    def is_empty(self): return self.count == 0
    def is_full(self): return self.count == self.capacity
    def enqueue(self, value):
        if self.is_full(): return False
        self.data[self.rear_index] = value
        self.rear_index = (self.rear_index + 1) % self.capacity
        self.count += 1
        return True
    def dequeue(self):
        if self.is_empty(): return None
        value = self.data[self.front_index]
        self.data[self.front_index] = None
        self.front_index = (self.front_index + 1) % self.capacity
        self.count -= 1
        return value
    def front(self): return self.data[self.front_index] if not self.is_empty() else None

def reverse_queue(q):
    stack = []
    while q: stack.append(q.popleft())
    while stack: q.append(stack.pop())
    return q

def generate_binary_numbers(n):
    result, q = [], deque(["1"])
    for _ in range(n):
        x = q.popleft(); result.append(x)
        q.append(x + "0"); q.append(x + "1")
    return result

def bfs(graph, start):
    visited, q, result = {start}, deque([start]), []
    while q:
        node = q.popleft(); result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor); q.append(neighbor)
    return result

if __name__ == "__main__":
    q = Queue(); q.enqueue(10); q.enqueue(20); q.enqueue(30)
    q.display(); print("Front:", q.front()); print("Dequeue:", q.dequeue()); q.display()
    print("Binary:", generate_binary_numbers(5))
    print("BFS:", bfs({0:[1,2],1:[3],2:[4],3:[],4:[]}, 0))

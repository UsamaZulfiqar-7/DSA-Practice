"""Day 12: Heap and Priority Queue examples using Python's heapq."""
import heapq
from itertools import count


def heap_demo():
    heap = []
    for value in [7, 2, 9, 1, 5]:
        heapq.heappush(heap, value)
    print("Min-heap internal list:", heap)
    print("Smallest item (peek):", heap[0])
    print("Pop in ascending order:", [heapq.heappop(heap) for _ in range(len(heap))])


def max_heap_demo():
    values = [7, 2, 9, 1, 5]
    heap = [-value for value in values]
    heapq.heapify(heap)
    print("Pop in descending order:", [-heapq.heappop(heap) for _ in range(len(heap))])


class PriorityQueue:
    """Lower numeric priority is served first; ties preserve insertion order."""
    def __init__(self):
        self._heap = []
        self._counter = count()

    def push(self, item, priority):
        heapq.heappush(self._heap, (priority, next(self._counter), item))

    def pop(self):
        if not self._heap:
            raise IndexError("pop from an empty priority queue")
        priority, _, item = heapq.heappop(self._heap)
        return item, priority

    def peek(self):
        if not self._heap:
            raise IndexError("peek from an empty priority queue")
        priority, _, item = self._heap[0]
        return item, priority

    def is_empty(self):
        return not self._heap

    def __len__(self):
        return len(self._heap)


def main():
    print("MIN-HEAP")
    heap_demo()
    print("\nMAX-HEAP")
    max_heap_demo()
    print("\nPRIORITY QUEUE")
    tasks = PriorityQueue()
    tasks.push("Write report", 3)
    tasks.push("Fix production bug", 1)
    tasks.push("Reply to email", 2)
    print("Next task:", tasks.peek())
    while not tasks.is_empty():
        print("Serving:", tasks.pop())


if __name__ == "__main__":
    main()

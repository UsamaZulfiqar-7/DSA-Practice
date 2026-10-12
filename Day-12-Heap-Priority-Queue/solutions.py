"""Reference solutions for selected Day 12 heap exercises."""
import heapq
from collections import Counter


def k_largest(values, k):
    if k < 0:
        raise ValueError("k must be non-negative")
    return heapq.nlargest(k, values)


def kth_largest(values, k):
    if k < 1 or k > len(values):
        raise ValueError("k must be between 1 and len(values)")
    top_k = []
    for value in values:
        if len(top_k) < k:
            heapq.heappush(top_k, value)
        elif value > top_k[0]:
            heapq.heapreplace(top_k, value)
    return top_k[0]


def kth_smallest(values, k):
    if k < 1 or k > len(values):
        raise ValueError("k must be between 1 and len(values)")
    return heapq.nsmallest(k, values)[-1]


def top_k_frequent(values, k):
    counts = Counter(values)
    return heapq.nlargest(k, counts.keys(), key=counts.get)


def merge_sorted_lists(first, second):
    """Merge two ascending lists using a min-heap."""
    heap = []
    lists = (first, second)
    for list_id, values in enumerate(lists):
        if values:
            heapq.heappush(heap, (values[0], list_id, 0))
    result = []
    while heap:
        value, list_id, index = heapq.heappop(heap)
        result.append(value)
        next_index = index + 1
        if next_index < len(lists[list_id]):
            heapq.heappush(heap, (lists[list_id][next_index], list_id, next_index))
    return result


def main():
    values = [7, 2, 9, 1, 5, 8, 3]
    print("3 largest:", k_largest(values, 3))
    print("3rd largest:", kth_largest(values, 3))
    print("4th smallest:", kth_smallest(values, 4))
    print("Top 2 frequent:", top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    print("Merged:", merge_sorted_lists([1, 4, 7], [2, 3, 8]))

if __name__ == "__main__":
    main()

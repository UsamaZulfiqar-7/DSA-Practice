# Day 5 Practice — Solutions

## 1. Linear Search True/False
```python
def contains(arr, target):
    for value in arr:
        if value == target:
            return True
    return False
```

## 2. First Index
```python
def first_index(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1
```

## 3. Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## 4. Binary Search Comparisons
Count each time `arr[mid]` is checked. The number is O(log n).

## 5. Bubble Sort Descending
```python
def bubble_desc(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

## 6. Selection Sort Descending
```python
def selection_desc(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr
```

## 7. Insertion Sort Strings
```python
def insertion_strings(words):
    words = words.copy()
    for i in range(1, len(words)):
        key = words[i]
        j = i - 1
        while j >= 0 and words[j] > key:
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = key
    return words
```

## 8. Second Smallest
```python
def second_smallest(arr):
    values = sorted(set(arr))
    return values[1] if len(values) >= 2 else None
```

## 9. Sort and Remove Duplicates
```python
def sort_unique(arr):
    return sorted(set(arr))
```

## 10. Two Numbers in Sorted Array
Use two pointers: one at the beginning and one at the end.
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return (arr[left], arr[right])
        if total < target:
            left += 1
        else:
            right -= 1
    return None
```

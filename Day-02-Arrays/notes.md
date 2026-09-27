# Arrays — Notes

## 1. What is an Array?
An array stores multiple values in an ordered sequence.

```python
numbers = [10, 20, 30, 40, 50]
```

Conceptually:

```text
Index:   0   1   2   3   4
Value:  10  20  30  40  50
```

Python uses `list` as its common flexible array-like structure.

## 2. Indexing
Indexes normally start at `0`.

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[0])  # 10
print(numbers[2])  # 30
```

**Time: O(1)**

## 3. Updating

```python
numbers[2] = 100
```

**Time: O(1)**

## 4. Traversal

```python
for value in numbers:
    print(value)
```

**Time: O(n)**, **Extra Space: O(1)**

## 5. Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

Best case: `O(1)`  
Worst case: `O(n)`  
Extra Space: `O(1)`

## 6. Insertion

Adding at the end:

```python
numbers.append(40)
```

Python list append is **amortized O(1)**.

Insertion at the beginning/middle may shift elements:

```python
numbers.insert(1, 99)
```

Typical complexity: **O(n)**

## 7. Deletion

```python
numbers.pop(1)
```

Deleting from the beginning/middle may shift elements.

Typical complexity: **O(n)**.

Removing the last element with `pop()` is generally **O(1)**.

## 8. Minimum and Maximum

```python
def find_min(arr):
    minimum = arr[0]
    for value in arr:
        if value < minimum:
            minimum = value
    return minimum
```

Finding min/max requires checking the elements.

**Time: O(n)**, **Extra Space: O(1)**

## 9. Sum

```python
def array_sum(arr):
    total = 0
    for value in arr:
        total += value
    return total
```

**Time: O(n)**, **Extra Space: O(1)**

## 10. Reverse with Two Pointers

```python
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr
```

**Time: O(n)**, **Extra Space: O(1)**

## 11. Count Occurrences

```python
def count_occurrences(arr, target):
    count = 0
    for value in arr:
        if value == target:
            count += 1
    return count
```

**Time: O(n)**, **Extra Space: O(1)**

## 12. Common Array Operation Complexity

| Operation | Typical Complexity |
|---|---:|
| Access by index | O(1) |
| Update by index | O(1) |
| Traversal | O(n) |
| Linear Search | O(n) |
| Append at end | Amortized O(1) |
| Insert beginning/middle | O(n) |
| Delete beginning/middle | O(n) |
| Find minimum | O(n) |
| Find maximum | O(n) |
| Sum | O(n) |
| Reverse | O(n) |

## Key Takeaways
- Index access is fast: `O(1)`.
- Traversal/search generally require `O(n)`.
- Beginning/middle insertion or deletion can be `O(n)` because elements may need to shift.
- Reversing with two pointers can be done in `O(n)` time and `O(1)` extra space.

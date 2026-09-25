# Time & Space Complexity

## 1. What is Time Complexity?

Time complexity describes how the number of operations performed by an algorithm grows as the input size `n` increases.

It does **not** mean the exact time in seconds. It describes the growth rate of an algorithm.

---

## 2. What is Space Complexity?

Space complexity describes how much **extra memory** an algorithm needs as the input size grows.

---

## 3. Common Big O Complexities

| Complexity | Name | Common Example |
|---|---|---|
| `O(1)` | Constant | Accessing an array element |
| `O(log n)` | Logarithmic | Binary Search |
| `O(n)` | Linear | Traversing an array |
| `O(n log n)` | Linearithmic | Merge Sort |
| `O(n²)` | Quadratic | Nested loops |
| `O(2ⁿ)` | Exponential | Some recursive algorithms |
| `O(n!)` | Factorial | Generating permutations |

### General order

`O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)`

---

## 4. O(1) — Constant Time

```python
def get_first(arr):
    return arr[0]
```

The first element is accessed directly regardless of the array size.

**Time:** `O(1)`  
**Extra Space:** `O(1)`

---

## 5. O(n) — Linear Time

```python
def print_array(arr):
    for item in arr:
        print(item)
```

The loop runs once for every element.

**Time:** `O(n)`  
**Extra Space:** `O(1)`

---

## 6. O(n²) — Quadratic Time

```python
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
```

For every element, the inner loop processes all elements.

`n × n = n²`

**Time:** `O(n²)`  
**Extra Space:** `O(1)`

---

## 7. Separate Loops

```python
def example(arr):
    for x in arr:
        print(x)

    for y in arr:
        print(y)
```

The work is:

`n + n = 2n`

Constants are ignored in Big O:

`O(2n) = O(n)`

**Time:** `O(n)`

---

## 8. O(log n) — Logarithmic Time

```python
def example(n):
    i = 1

    while i < n:
        i *= 2
```

The value doubles each iteration:

`1 → 2 → 4 → 8 → 16 → ...`

The number of iterations grows logarithmically.

**Time:** `O(log n)`  
**Extra Space:** `O(1)`

Binary Search is a major example of an `O(log n)` algorithm.

---

## 9. O(n log n)

A common example is Merge Sort.

Merge Sort repeatedly divides the input and then combines the results efficiently.

**Time:** `O(n log n)`

We will study Merge Sort in a later topic.

---

## 10. Space Complexity Example — O(n)

```python
def create_array(n):
    result = []

    for i in range(n):
        result.append(i)

    return result
```

The `result` list stores `n` elements.

**Time:** `O(n)`  
**Extra Space:** `O(n)`

---

## 11. Nested Loops

```python
def example(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```

Outer loop = `n` operations  
Inner loop = `n` operations for each outer iteration

Therefore:

`n × n = n²`

**Time:** `O(n²)`  
**Extra Space:** `O(1)`

---

## 12. Triple Nested Loop

```python
def example(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
```

Therefore:

`n × n × n = n³`

**Time:** `O(n³)`  
**Extra Space:** `O(1)`

---

## 13. Quick Rules to Remember

### Rule 1 — Drop constants

`O(2n)` → `O(n)`

`O(5n)` → `O(n)`

### Rule 2 — Keep the highest-growing term

`O(n² + n)` → `O(n²)`

`O(n³ + n² + n)` → `O(n³)`

### Rule 3 — Separate loops usually add

`O(n) + O(n)` → `O(n)`

### Rule 4 — Nested loops usually multiply

`O(n) × O(n)` → `O(n²)`

---

## 14. Summary

Before moving to the next DSA topic, you should be able to identify:

- `O(1)` — Constant
- `O(log n)` — Logarithmic
- `O(n)` — Linear
- `O(n log n)` — Linearithmic
- `O(n²)` — Quadratic
- `O(2ⁿ)` — Exponential
- `O(n!)` — Factorial
- Time Complexity
- Space Complexity
- Separate vs nested loops
- Why constants are ignored
- Why the highest-growing term matters

# Hashing / HashMap — Notes

## 1. What is Hashing?

Hashing is a technique that converts a key into an index/location where its associated data can be stored or found efficiently.

Conceptually:

```text
Key → Hash Function → Hash Value / Index → Stored Value
```

For example:

```text
"apple" → hash function → location → 50
```

The exact internal implementation is handled by Python.

---

## 2. What is a HashMap?

A HashMap stores data as **key-value pairs**.

Example:

```python
student = {
    "name": "Usama",
    "age": 22,
    "city": "Rawalpindi"
}
```

Here:

- `name`, `age`, `city` are keys
- `Usama`, `22`, `Rawalpindi` are values

Python's `dict` is commonly used as a HashMap in DSA problems.

---

## 3. Creating a Dictionary

```python
marks = {
    "Ali": 85,
    "Ahmed": 90,
    "Usama": 95
}
```

Empty dictionary:

```python
data = {}
```

---

## 4. Accessing Values

```python
marks = {"Ali": 85, "Usama": 95}

print(marks["Usama"])
```

Output:

```text
95
```

Safer option:

```python
print(marks.get("Usama"))
print(marks.get("Unknown", 0))
```

---

## 5. Insert and Update

Insert:

```python
marks["Hamza"] = 88
```

Update:

```python
marks["Hamza"] = 92
```

If the key already exists, its value is replaced.

---

## 6. Check Whether a Key Exists

```python
if "Usama" in marks:
    print("Key exists")
```

This is very common in DSA problems.

---

## 7. Delete

```python
del marks["Ali"]
```

Or:

```python
marks.pop("Ali", None)
```

---

## 8. Traversing a HashMap

Keys:

```python
for key in marks:
    print(key)
```

Keys and values:

```python
for key, value in marks.items():
    print(key, value)
```

---

## 9. Frequency Counting

One of the most important HashMap patterns is counting occurrences.

```python
nums = [1, 2, 2, 3, 1, 2]
frequency = {}

for num in nums:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)
```

Result:

```text
{1: 2, 2: 3, 3: 1}
```

This pattern is extremely useful.

---

## 10. Find Duplicates

```python
nums = [1, 2, 3, 2, 4, 1]
seen = set()
duplicates = []

for num in nums:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)
```

A `set` is also hash-based and is useful when only membership is needed.

---

## 11. Two Sum Pattern

Problem: Find two numbers whose sum equals the target.

Example:

```text
nums = [2, 7, 11, 15]
target = 9
```

Instead of checking every pair in O(n²), store previously seen values in a HashMap.

For each number:

```text
needed = target - current
```

If `needed` is already in the HashMap, we found the pair.

Typical complexity:

- Time: O(n)
- Space: O(n)

---

## 12. HashMap vs Set

### Dictionary

Stores key-value pairs.

```python
student = {"name": "Usama", "age": 22}
```

### Set

Stores unique values.

```python
numbers = {1, 2, 3}
```

Use a dictionary when you need associated information/counts. Use a set when you mainly need fast membership and uniqueness.

---

## 13. Important Pattern

Whenever you see problems involving:

- frequency
- duplicates
- counting
- fast lookup
- unique values
- pair matching
- previously seen elements

Think about **HashMap / Set**.

---

## 14. Complexity

For Python dictionary/set operations, the expected average complexity is:

| Operation | Average |
|---|---:|
| Insert | O(1) |
| Search | O(1) |
| Delete | O(1) |

A complete traversal is O(n).

---

## 15. Key Takeaway

The most important skill today is not memorizing `dict` syntax. It is recognizing:

> **Can I store previously seen information so I do not have to search the whole list again?**

If yes, HashMap may turn an O(n²) solution into O(n).

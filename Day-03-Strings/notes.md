# Strings — Notes

## 1. What is a String?
A string is a sequence of characters.

```python
name = "Usama"
```

Conceptually:

```text
Index:   0   1   2   3   4
Char:    U   s   a   m   a
```

Python strings are immutable, so an existing string cannot be changed character-by-character.

## 2. Indexing

```python
text = "Python"
print(text[0])  # P
print(text[2])  # t
```

Direct access is generally `O(1)`.

## 3. Traversal

```python
for char in text:
    print(char)
```

Time: `O(n)`.

## 4. Reverse

```python
text = "Python"
print(text[::-1])
```

A two-pointer implementation can also be used by converting the string to a list.

Time: `O(n)`; extra space: `O(n)` for a character list.

## 5. Palindrome
A palindrome reads the same forward and backward, such as `madam` or `level`.

```python
def is_palindrome(text):
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True
```

Time: `O(n)`; extra space: `O(1)`.

## 6. Character Frequency

```python
def character_frequency(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
```

Average time: `O(n)`; extra space: `O(k)`, where `k` is the number of distinct characters.

## 7. First Non-Repeating Character
Count frequencies first, then scan the original string to find the first character with frequency `1`.

## 8. Anagram
Two strings are anagrams when they contain the same characters with the same frequencies.

Examples: `listen` and `silent`.

A frequency dictionary gives average `O(n)` time.

## 9. Remove Spaces
A list plus `join()` is generally preferable to repeated string concatenation.

## 10. Useful Complexity Table

| Operation / Problem | Typical Complexity |
|---|---:|
| Access character by index | O(1) |
| Traverse string | O(n) |
| Reverse | O(n) |
| Palindrome check | O(n) |
| Count characters | O(n) |
| Character frequency | O(n) average |
| First non-repeating | O(n) average |
| Anagram check | O(n) average |

## Key Takeaways
- Strings are sequences of characters.
- Python strings are immutable.
- Traversal usually takes `O(n)`.
- Two pointers are useful for palindrome problems.
- Frequency maps are useful for counting, anagrams, duplicates and unique-character problems.

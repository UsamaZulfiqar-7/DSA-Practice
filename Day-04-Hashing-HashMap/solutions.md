# Day 4 — Practice Solutions

Use this file only after attempting the questions in `practice.py` yourself.

## Q1. Frequency of Numbers

```python
def q1_frequency(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return freq
```

Time: O(n) average. Space: O(n).

## Q2. Character Frequency

```python
def q2_character_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq
```

Time: O(n). Space: O(k), where k is the number of distinct characters.

## Q3. Contains Duplicate

```python
def q3_contains_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    return False
```

Time: O(n) average. Space: O(n).

## Q4. First Non-Repeating Character

```python
def q4_first_non_repeating(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    for char in text:
        if freq[char] == 1:
            return char
    return None
```

Time: O(n). Space: O(k).

## Q5. Two Sum

```python
def q5_two_sum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]
        seen[num] = i
    return []
```

Time: O(n) average. Space: O(n).

## Q6. Find Duplicate Values

```python
def q6_find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)
```

Time: O(n) average. Space: O(n).

## Q7. Anagram Check

```python
def q7_is_anagram(first, second):
    if len(first) != len(second):
        return False

    freq = {}
    for char in first:
        freq[char] = freq.get(char, 0) + 1

    for char in second:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False

    return True
```

Time: O(n). Space: O(k).

## Q8. Majority Element

```python
def q8_majority_element(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1

    for num, count in freq.items():
        if count > len(numbers) // 2:
            return num
```

Time: O(n) average. Space: O(n).

## Q9. Intersection of Two Arrays

```python
def q9_intersection(first, second):
    second_set = set(second)
    result = set()

    for num in first:
        if num in second_set:
            result.add(num)

    return list(result)
```

Time: O(n + m) average. Space: O(n + m).

## Q10. Group Words by First Character

```python
def q10_group_words(words):
    groups = {}

    for word in words:
        if not word:
            continue
        key = word[0]
        groups.setdefault(key, []).append(word)

    return groups
```

Time: O(total characters/words processed), excluding output-copy details. Space: O(n) for the groups.

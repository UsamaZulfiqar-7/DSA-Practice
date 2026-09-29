"""Day 4 - Hashing / HashMap
Practical Python implementations.
"""


def basic_dictionary_operations():
    student = {"name": "Usama", "age": 22, "cgpa": 3.85}

    print("Original:", student)
    print("Name:", student["name"])

    # Insert
    student["city"] = "Rawalpindi"

    # Update
    student["age"] = 23

    # Safe lookup
    print("Phone:", student.get("phone", "Not available"))

    # Membership
    print("cgpa" in student)

    # Delete
    student.pop("city", None)

    print("Final:", student)


def frequency_count(numbers):
    frequency = {}

    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    return frequency


def character_frequency(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency


def first_non_repeating_character(text):
    frequency = character_frequency(text)

    for char in text:
        if frequency[char] == 1:
            return char

    return None


def contains_duplicate(numbers):
    seen = set()

    for num in numbers:
        if num in seen:
            return True
        seen.add(num)

    return False


def two_sum(numbers, target):
    """Return indices of two numbers whose sum equals target."""
    seen = {}

    for i, num in enumerate(numbers):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

    return []


def count_words(text):
    words = text.lower().split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def find_duplicates(numbers):
    seen = set()
    duplicates = []

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates


def group_by_remainder(numbers, divisor):
    """Group numbers by their remainder when divided by divisor."""
    groups = {}

    for num in numbers:
        key = num % divisor
        groups.setdefault(key, []).append(num)

    return groups


if __name__ == "__main__":
    print("--- Basic Dictionary Operations ---")
    basic_dictionary_operations()

    nums = [1, 2, 2, 3, 1, 2, 4]
    print("\nFrequency:", frequency_count(nums))

    text = "programming"
    print("Character frequency:", character_frequency(text))
    print("First non-repeating:", first_non_repeating_character(text))

    print("Contains duplicate:", contains_duplicate([1, 2, 3, 2]))
    print("Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("Word frequency:", count_words("data science data analytics"))
    print("Duplicates:", find_duplicates([1, 2, 3, 2, 4, 1, 2]))
    print("Groups:", group_by_remainder([1, 2, 3, 4, 5, 6, 7], 3))

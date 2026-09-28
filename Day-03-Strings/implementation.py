# Day 3 - Strings


def reverse_string(text):
    chars = list(text)
    left = 0
    right = len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


def is_palindrome(text):
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


def count_consonants(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in vowels:
            count += 1
    return count


def character_frequency(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def first_non_repeating(text):
    frequency = character_frequency(text)
    for char in text:
        if frequency[char] == 1:
            return char
    return None


def are_anagrams(first, second):
    if len(first) != len(second):
        return False
    frequency = {}
    for char in first:
        frequency[char] = frequency.get(char, 0) + 1
    for char in second:
        if char not in frequency:
            return False
        frequency[char] -= 1
        if frequency[char] < 0:
            return False
    return True


def remove_spaces(text):
    chars = []
    for char in text:
        if char != " ":
            chars.append(char)
    return "".join(chars)


def count_words(text):
    return len(text.split())


# Examples
text = "madam"
print("Original:", text)
print("Reversed:", reverse_string(text))
print("Palindrome:", is_palindrome(text))
print("Vowels:", count_vowels(text))
print("Consonants:", count_consonants(text))
print("Frequency:", character_frequency(text))
print("First non-repeating:", first_non_repeating(text))
print("Anagram test:", are_anagrams("listen", "silent"))
print("Words:", count_words("I am learning DSA"))

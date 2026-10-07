# Day 9 — Recursion Implementation

def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def sum_n(n):
    if n <= 0:
        return 0
    return n + sum_n(n - 1)

def power(base, exponent):
    if exponent < 0:
        raise ValueError("Use a non-negative exponent")
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def reverse_string(text):
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]

def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

def array_sum(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + array_sum(arr, index + 1)

def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    return binary_search(arr, target, mid + 1, right)

def gcd(a, b):
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)

def count_occurrences(arr, target, index=0):
    if index == len(arr):
        return 0
    return (arr[index] == target) + count_occurrences(arr, target, index + 1)

if __name__ == "__main__":
    print("Factorial 5:", factorial(5))
    print("Sum 1..5:", sum_n(5))
    print("2^5:", power(2, 5))
    print("Fibonacci 7:", fibonacci(7))
    print("Reverse:", reverse_string("Python"))
    print("Palindrome:", is_palindrome("level"))
    print("Array sum:", array_sum([1, 2, 3, 4, 5]))
    print("Binary search:", binary_search([1, 3, 5, 7, 9], 7))
    print("GCD:", gcd(48, 18))
    print("Count 2:", count_occurrences([2, 1, 2, 3, 2], 2))

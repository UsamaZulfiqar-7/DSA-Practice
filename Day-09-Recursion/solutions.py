# Day 9 — Recursion Practice Solutions

def print_1_to_n(n, current=1):
    if current > n:
        return
    print(current)
    print_1_to_n(n, current + 1)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def sum_of_digits(number):
    number = abs(number)
    if number < 10:
        return number
    return number % 10 + sum_of_digits(number // 10)

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

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

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

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
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

def subsequences(text):
    result = []
    def backtrack(index, current):
        if index == len(text):
            result.append("".join(current))
            return
        backtrack(index + 1, current)
        current.append(text[index])
        backtrack(index + 1, current)
        current.pop()
    backtrack(0, [])
    return result

if __name__ == "__main__":
    print_1_to_n(5)
    print(factorial(5))
    print(sum_of_digits(1234))
    print(power(2, 5))
    print(reverse_string("hello"))
    print(is_palindrome("level"))
    print(fibonacci(6))
    print(binary_search([1, 3, 5, 7, 9], 7))
    print(gcd(48, 18))
    print(subsequences("abc"))

# Day 1 - Time & Space Complexity
# Examples for practice

# Example 1: O(1)
def get_first(arr):
    return arr[0]


# Example 2: O(n)
def print_array(arr):
    for item in arr:
        print(item)


# Example 3: O(n^2)
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)


# Example 4: O(log n)
def logarithmic_example(n):
    i = 1
    while i < n:
        i *= 2


# Example 5: O(n) time and O(n) extra space
def create_array(n):
    result = []

    for i in range(n):
        result.append(i)

    return result


# Example 6: O(n^3)
def triple_nested_loop(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

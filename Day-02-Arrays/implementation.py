# Day 2 - Arrays
# Python implementations and examples

def access_element(arr, index):
    return arr[index]


def update_element(arr, index, value):
    arr[index] = value
    return arr


def traverse_array(arr):
    for value in arr:
        print(value)


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def insert_element(arr, index, value):
    arr.insert(index, value)
    return arr


def delete_element(arr, index):
    arr.pop(index)
    return arr


def find_min(arr):
    minimum = arr[0]
    for value in arr:
        if value < minimum:
            minimum = value
    return minimum


def find_max(arr):
    maximum = arr[0]
    for value in arr:
        if value > maximum:
            maximum = value
    return maximum


def array_sum(arr):
    total = 0
    for value in arr:
        total += value
    return total


def array_average(arr):
    return array_sum(arr) / len(arr)


def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def count_occurrences(arr, target):
    count = 0
    for value in arr:
        if value == target:
            count += 1
    return count


# Example
numbers = [10, 20, 30, 40, 50]

print("Original:", numbers)
print("Index 2:", access_element(numbers, 2))

update_element(numbers, 2, 99)
print("After update:", numbers)

print("Search 40:", linear_search(numbers, 40))
print("Minimum:", find_min(numbers))
print("Maximum:", find_max(numbers))
print("Sum:", array_sum(numbers))
print("Average:", array_average(numbers))
print("Occurrences of 20:", count_occurrences(numbers, 20))

reverse_array(numbers)
print("Reversed:", numbers)

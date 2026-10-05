# Day 7 — Stack Implementation

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value): self.items.append(value)

    def pop(self):
        return None if self.is_empty() else self.items.pop()

    def peek(self):
        return None if self.is_empty() else self.items[-1]

    def is_empty(self): return len(self.items) == 0
    def size(self): return len(self.items)
    def display(self): print("Bottom ->", self.items, "<- Top")


def reverse_string(text):
    stack = list(text)
    result = []
    while stack:
        result.append(stack.pop())
    return "".join(result)


def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]: return False
            stack.pop()
    return not stack


def decimal_to_binary(number):
    if number == 0: return "0"
    stack = []
    while number > 0:
        stack.append(str(number % 2))
        number //= 2
    return "".join(reversed(stack))


def next_greater_elements(arr):
    result = [-1] * len(arr)
    stack = []
    for i, value in enumerate(arr):
        while stack and value > arr[stack[-1]]:
            result[stack.pop()] = value
        stack.append(i)
    return result


if __name__ == "__main__":
    stack = Stack()
    for value in [10, 20, 30]: stack.push(value)
    stack.display()
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Reverse:", reverse_string("Python"))
    print("Balanced:", is_balanced("{[()]}"))
    print("13 in binary:", decimal_to_binary(13))
    print("Next greater:", next_greater_elements([4, 5, 2, 10, 8]))

# Day 7 — Stack Practice Solutions

class Stack:
    def __init__(self): self.items = []
    def push(self, value): self.items.append(value)
    def pop(self): return None if not self.items else self.items.pop()
    def peek(self): return None if not self.items else self.items[-1]
    def is_empty(self): return not self.items
    def size(self): return len(self.items)


def reverse_string(text):
    stack = list(text); result = []
    while stack: result.append(stack.pop())
    return ''.join(result)


def is_balanced(expression):
    stack = []; pairs = {')':'(', ']':'[', '}':'{'}
    for char in expression:
        if char in '([{': stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]: return False
            stack.pop()
    return not stack


def remove_duplicates(text):
    stack = []
    for char in text:
        if stack and stack[-1] == char: stack.pop()
        else: stack.append(char)
    return ''.join(stack)


def decimal_to_binary(number):
    if number == 0: return '0'
    stack = []
    while number:
        stack.append(str(number % 2)); number //= 2
    return ''.join(reversed(stack))


def next_greater_elements(arr):
    result = [-1] * len(arr); stack = []
    for i, value in enumerate(arr):
        while stack and value > arr[stack[-1]]:
            result[stack.pop()] = value
        stack.append(i)
    return result


def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.lstrip('-').isdigit(): stack.append(int(token)); continue
        right, left = stack.pop(), stack.pop()
        if token == '+': stack.append(left + right)
        elif token == '-': stack.append(left - right)
        elif token == '*': stack.append(left * right)
        elif token == '/': stack.append(int(left / right))
    return stack[-1]


def stock_span(prices):
    spans = [0] * len(prices); stack = []
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] <= price: stack.pop()
        spans[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    return spans


class MinStack:
    def __init__(self): self.stack = []; self.min_stack = []
    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]: self.min_stack.append(value)
    def pop(self):
        if not self.stack: return None
        value = self.stack.pop()
        if value == self.min_stack[-1]: self.min_stack.pop()
        return value
    def top(self): return None if not self.stack else self.stack[-1]
    def get_min(self): return None if not self.min_stack else self.min_stack[-1]


if __name__ == '__main__':
    print(reverse_string('hello'))
    print(is_balanced('{[()]}'))
    print(remove_duplicates('abbaca'))
    print(decimal_to_binary(13))
    print(next_greater_elements([4,5,2,10,8]))
    print(evaluate_postfix('2 3 + 4 *'))
    print(stock_span([100,80,60,70,60,75,85]))

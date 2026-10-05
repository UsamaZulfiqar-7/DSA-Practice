# Stack Notes

## LIFO
Last In, First Out. Think of a stack of plates: the last plate placed is normally the first removed.

## Python List as Stack
```python
stack = []
stack.append(10)   # push
stack.append(20)
top = stack[-1]    # peek
item = stack.pop() # pop
```

## Balanced Parentheses
Push opening brackets. For a closing bracket, compare it with the stack top. At the end the stack must be empty.

## Reverse String
Push characters and pop them; the last character comes out first.

## Monotonic Stack
A stack maintained in increasing/decreasing order. Common problems include Next Greater Element, Daily Temperatures and Stock Span.

## Complexity
Normal stack operations are O(1), while searching is O(n). Space is O(n).

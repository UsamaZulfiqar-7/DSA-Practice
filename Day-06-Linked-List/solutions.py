# Day 6 — Linked List Practice Solutions

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_list(values):
    head = tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


def search(head, target):
    position = 0
    current = head
    while current:
        if current.data == target:
            return position
        current = current.next
        position += 1
    return -1


def insert_at_beginning(head, value):
    node = Node(value)
    node.next = head
    return node


def insert_at_end(head, value):
    node = Node(value)
    if head is None:
        return node
    current = head
    while current.next:
        current = current.next
    current.next = node
    return head


def delete_value(head, value):
    if head is None:
        return None
    if head.data == value:
        return head.next
    current = head
    while current.next:
        if current.next.data == value:
            current.next = current.next.next
            break
        current = current.next
    return head


def reverse(head):
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    head = create_list([10, 20, 30, 40, 50])
    print("Original:")
    display(head)
    print("Length:", length(head))
    print("Search 30:", search(head, 30))
    head = insert_at_beginning(head, 5)
    head = insert_at_end(head, 60)
    head = delete_value(head, 30)
    print("After updates:")
    display(head)
    print("Middle:", find_middle(head))
    head = reverse(head)
    print("Reversed:")
    display(head)
    print("Has cycle:", has_cycle(head))

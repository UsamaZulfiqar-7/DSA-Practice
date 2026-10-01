# Day 6 — Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise ValueError("Position cannot be negative")
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        if current is None:
            raise IndexError("Position out of range")
        new_node.next = current.next
        current.next = new_node

    def delete(self, value):
        if self.head is None:
            return False
        if self.head.data == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def display(self):
        print(" -> ".join(map(str, self.to_list())) + " -> None")


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_position(15, 2)

    print("List:")
    linked_list.display()
    print("Search 20:", linked_list.search(20))
    print("Length:", linked_list.length())

    linked_list.delete(15)
    print("After deleting 15:")
    linked_list.display()

    linked_list.reverse()
    print("Reversed:")
    linked_list.display()

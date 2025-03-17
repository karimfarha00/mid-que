# Implement a function to reverse a singly linked list in Python:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_List(self):
        current = self.head
        while current:
            print(current.data, end="--->")
            current = current.next
        print("None")

s = LinkedList()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
print("Original list:")
s.print_List()
s.reverse()
print("Reversed list:")
s.print_List()
    
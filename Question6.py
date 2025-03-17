# Identify the logical error in this queue implementation and fix it:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head==None and self.tail==None

    # Adding a node
    def enqueue(self, node):
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # Removing a node
    def dequeue(self):
        if self.isEmpty():
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp

    def printQueue(self):
        current = self.head
        while current==None:
            print(current.data)
            current = current.next


print("===== Bank Queue Example =====")
bank_queue = Queue()


bank_queue.enqueue(Node("Customer:Karim"))
bank_queue.enqueue(Node("Customer:Hadi"))
bank_queue.enqueue(Node("Customer:Ahmad"))
bank_queue.enqueue(Node("Customer:Taha"))

print("===== Queue State =====")
bank_queue.printQueue()


print("===== Serving Customers =====")
bank_queue.dequeue()
bank_queue.dequeue()

print("===== Queue State After Serving =====")
bank_queue.printQueue()
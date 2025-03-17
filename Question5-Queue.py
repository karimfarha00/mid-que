class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def isEmpty(self):
        return self.head==None and self.tail==None
            
            
    def enqueue(self,node):
        if self.isEmpty():
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            temp=self.head
            self.head=self.head.next
            return temp.data
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
            print()
#FIFO (First In First Out)
q=Queue()
print("========Enqueue The Grade========")
q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.enqueue(Node(50))
q.display()
print("========Dequeue The Grade========")
q.dequeue()
q.display()
        
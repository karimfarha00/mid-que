class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def printStack(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.next
    def push(self,node):
        node.next=self.head
        self.head=node
        
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:
            temp=self.head
            self.head=self.head.next
            return temp    
s=Stack()
print("======Pushing The Customer Name In Bank======")
s.push(Node("Taha"))
s.push(Node("karim"))
s.push(Node("Houda"))
s.printStack()
print("======Poping The Customer Name In Bank======")
#LIFO (Last In First Out) 
s.pop()
s.printStack()
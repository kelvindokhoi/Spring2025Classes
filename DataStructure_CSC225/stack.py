# stack.py

class Node:
    def __init__(self,v):
        self.val = v
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def isEmpty(self):
        return self.size == 0
    def peek(self):
        if self.head is None:
            raise ValueError
        return self.head.val
    def push(self,var):
        newNode = Node(var)
        newNode.next = self.head
        self.head = newNode
        self.size+=1
    def getSize(self):
        return self.size
    def pop(self):
        if self.head is None:
            raise ValueError
        v = self.head.val
        self.head = self.head.next
        self.size-=1
        return v
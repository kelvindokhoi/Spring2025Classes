# doublyLinkedList.py

class Node:
    def __init__(self,v):
        self.var=v
        self.next=None
        self.prev=None
        

class Deque:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length = 0
    def addtoHead(self, v): #O(1)
        self.length+=1
        newNode = Node(v)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head.prev=newNode
        self.head = newNode
    
    def removeHead(self):
        if self.head is None:return
        self.length-=1
        if self.head ==self.tail:
            self.head=None
            self.tail=None
            return
        self.head = self.head.next
        self.head.prev=None

    def addtoTail(self,v):
        self.length+=1
        newNode = Node(v)
        if self.tail is None:
            self.tail = newNode
            self.head = newNode   
        else:
            self.tail.next = newNode
            newNode.prev=self.tail
            self.tail = newNode
    def removeTail(self):
        if self.head is None:return
        self.length-=1
        if self.head ==self.tail:
            self.head=None
            self.tail=None
            return
        else:
            self.tail=self.tail.prev
            self.tail.next=None
    def __str__(self):
        s='';p = self.head
        while p is not None:
            if s=='':s=str(p.var)
            else:s = f"{s} {p.var}"
            p=p.next
        return s
    def rm(self,value):
        p=self.head
        if p is None or self.tail is None:return
        self.length -=1
        if self.head.var == value:
            if self.head==self.tail:self.head=None;self.tail=None;return
            else:self.head=self.head.next;self.head.prev=None;return
        if self.tail.var == value:
            if self.head==self.tail:self.head=None;self.tail=None;return
            self.tail=self.tail.prev;self.tail.next=None
        while p.next is not None:
            p=p.next
            if p.var == value:p.prev.next=p.next;p.next.prev=p.prev;return
        return
    def __iter__(self):
        return DequeIterator(self.tail)
    def getlen(self):
        return self.length
    # def printBackward(self):
    #     p.self.tail
class DequeIterator:
    def __init__(self,tail):
        self.current = tail
    def __next__(self):
        if self.current is None:
            raise StopIteration
        element = self.current.var
        self.current = self.current.prev
        return element
mylist=Deque()
print("1: add to head")
print("2: add to tail")
print("3: remove head")
print("4: rm tail")
print("5: print length")
print("6: iterate and print")
print("7: remove a specific value")
while True:
    n=int(input("Your choice: "))
    if n==1:
        mylist.addtoHead(int(input("Your num: ")))
        print(mylist)
    if n==2:
        mylist.addtoTail(int(input("Your num: ")))
        print(mylist)
    if n==3:
        mylist.removeHead()
        print(mylist)
    if n==4:
        mylist.removeTail()
        print(mylist)
    if n==5:
        print(mylist.getlen())
    if n==6:
        for v in mylist:
            print(v)
    if n==7:
        mylist.rm(int(input("Remove what? ")))
        print(mylist)

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
    def addtoHead(self, v):
        newNode = Node(v)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head.prev=newNode
        self.head = newNode
    
    def removeHead(self):
        if self.head is None:
            return
        if self.head ==self.tail:
            self.head=None
            self.tail=None
            return
        self.head = self.head.next
        self.head.prev=None

    def addtoTail(self,v):
        newNode = Node(v)
        if self.tail is None:
            self.tail = newNode
            self.head = newNode   
        else:
            self.tail.next = newNode
            newNode.prev=self.tail
            self.tail = newNode
    def removeTail(self):
        if self.head is None:
            return
        if self.head ==self.tail:
            self.head=None
            self.tail=None
            return
        else:
            self.tail=self.tail.prev
            self.tail.next=None
    def __str__(self):
        s=''
        p = self.head
        while p is not None:
            if s=='':
                s=str(p.var)
            else:
                s = f"{s} {p.var}"
            p=p.next
        return s
    def len(self):
        s=0
        p = self.head
        while p is not None:
            s+=1
            p=p.next
        return s
    # def printBackward(self):
    #     p.self.tail
mylist=Deque()
print("1: add to head")
print("2: add to tail")
print("3: remove head")
print("4: rm tail")
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
        print(mylist.len())

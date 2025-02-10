# doublyLinkedList_recoded.py

class Node:
    def __init__(self,var):
        self.var=var
        self.prev=None
        self.next=None
class Deque:
    def __init__(self):
        self.head=None
        self.tail=None
    def addHead(self,var):
        newNode= Node(var)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        newNode.next=self.head
        self.head.prev=newNode
        self.head = newNode
    def addTail(self,var):
        newNode= Node(var)
        if self.tail is None:
            self.head=newNode
            self.tail=newNode
            return
        newNode.prev=self.tail
        self.tail.next=newNode
        self.tail=newNode
    def rmHead(self):
        if self.head is None:return
        if self.head.next is None:
            self.head=None
            self.tail=None
            return
        self.head=self.head.next
        self.head.prev=None
    def rmTail(self):
        if self.tail is None:return
        if self.tail.prev is None:
            self.tail=None
            self.head=None
            return
        self.tail=self.tail.prev
        self.tail.next=None
    def __str__(self):
        p=self.head
        if p is None:
            return ""
        s=str(p.var)
        while p.next is not None:
            p=p.next
            s+=", "+str(p.var)
        return s
    def reversePrint(self):
        p=self.tail
        if p is None:
            return ""
        s=str(p.var)
        while p.prev is not None:
            p=p.prev
            s+=", "+str(p.var)
        return s
    def len(self):
        p=self.head
        if p is None:return 0
        t=1
        while p.next is not None:
            t+=1
            p=p.next
        return t
    def sum(self):
        p=self.head
        if p is None:return 0
        t=p.var
        while p.next is not None:
            p=p.next
            t+=p.var
        return t

def main():
    mylist = Deque()
    print(f"This is what the list looks like: [{mylist}]")
    while True:
        print("-------------------------")
        print("Your options are:")
        print("1: add to head")
        print("2: add to tail")
        print("3: remove head")
        print("4: remove tail")
        print("5: print list in reverse")
        print("6: print the length of the list")
        print("7: print the sum of the list")
        print("-------------------------")
        n = int(input("What is your choice? Type here: "))
        if n==1:
            mylist.addHead(int(input("Add what number to the head? Type here: ")))
        elif n==2:
            mylist.addTail(int(input("Add what number to the tail? Type here: ")))
        elif n==3:
            mylist.rmHead()
        elif n==4:
            mylist.rmTail()
        elif n==5:
            print(f"This is what the current list looks like in reverse: [{mylist.reversePrint()}]")
            continue
        elif n==6:
            print(f"The length of the list is: {mylist.len()}")
            continue
        elif n==7:
            print(f"The sum of the list is: {mylist.sum()}")
            continue
        print("-------------------------")
        print(f"This is the current list: [{mylist}]")

if __name__ == "__main__":
    main()
        
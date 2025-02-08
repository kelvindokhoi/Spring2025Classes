from math import inf

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def add(self,val):
        newNode = Node(val)
        newNode.next=self.head
        self.head = newNode
    def sumList(self):
        total = 0
        p=self.head
        while p is not None:
            total+=float(p.val)
            p=p.next
        return total
    def __str__(self):
        s=''
        p = self.head
        while p is not None:
            if s=='':
                s=str(p.val)
            else:
                s = f"{s} {p.val}"
            p=p.next
        return s
    def isAscending(self):
        p = self.head
        old=inf
        while p is not None:
            if p.val<=old:
                old=p.val
                p=p.next
            else:return False
        return True
    def delete(self,v):
        if self.head is None:
            return "Blankkk"
        p = self.head
        if p.val==v:
            self.head=p.next
            return "Succeeded"
        while p.next is not None:
            # check
            follow=p
            p=p.next
            if p.val==v:
                follow.next=p.next
                return "Succeeded"
        return f"What the hell you make me search smth that does not exist you notherducker"
    def add_end(self,v):
        p=self.head
        if p is None:
            self.head=Node(v)
            return
        while p.next is not None:
            p=p.next
        p.next=Node(v)
    def deleteHead(self):
        if self.head is None:
            return
        self.head=self.head.next



myList = LinkedList()
# addlist = [9,6,3,2,5]
addlist = []
for i in addlist:
    myList.add(i)
# myList.add(inf)
print(myList)
# print(myList.sumList())
# print(myList.isAscending())
# print(myList.delete(5))
# print(myList)
myList.add_end(99)
print(myList)
myList.add_end(99222222222222222)
print(myList)
myList.add_end(912346543465434569)
print(myList)
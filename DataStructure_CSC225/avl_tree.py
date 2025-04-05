# avl_tree

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val
        self.rb = 0
        self.lb = 0

class AVL_Tree:
    def __init__(self):
        self.root = None
    def add(self,value):
        newnode = Node(value)
        if self.root is None:
            self.root = newnode
            return
        # checked the root is empty
        if self.root.height == 1 and self.root.left is None and self.root.val>=value:
            newnode.parent = self.root
            self.root.left = newnode
            self.root.lb +=1
            return
        if self.root.height == 1 and self.root.right is None and self.root.val<value:
            newnode.parent = self.root
            self.root.right = newnode
            self.root.rb +=1
            return  
        # checked if there are only 2 or less than 2 nodes
        p = self.root
        while p is not None:
            if value > p.val:
                p = p.right
            else:
                p = p.left
        p = p.parent
        # found the place to insert
        newnode.parent = p
        if value>p.val:
            p.right = newnode
            p.rb +=1
        else:
            p.left = newnode
            p.lb +=1
        # inserted
        follow = p.val
        p = p.parent
        while p is not None:
            if p.val<follow:
                p.rb+=1
            else:
                p.lb-=1
            #-check for imbalance
            #if imba, rotate
            balance = p.rb - p.lb
            if abs(balance)<2:
                pass
            else:
                # check for RR
                if balance == 2:
                    if p.right.rb-p.right.lb>-1:
                        A = p
                        B = p.right
                        T2 = p.right.left
                        if A.parent is None:
                            # A is the ROOT
                            A.right = T2
                            T2.parent = A
                            A.parent = B
                            B.left = A
                            self.root = B
                        else:
                            # A is attached to something
                            A.right = T2
                            T2.parent = A
                            A.parent = B
                            B.left = A
                            B.parent = p.parent
                            if p.parent.val < p.val:
                                p.parent.right = B
                            else:
                                p.parent.left = B
                        return
                    else:
                        ...
                    # check for RL
                # check for LL
                elif balance ==-2:
                    if p.left.rb-p.left.lb<1:
                        ...
                    else:
                        ...
                    # check for LR
            follow = p.val
            p = p.parent
        # increment or decrement the whole parents


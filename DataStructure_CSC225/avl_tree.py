# magic_tree
# python avl_tree.py > avl_tree_out.txt

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val
        self.rb = 0
        self.lb = 0
    def __str__(self):
        return f"{self.val} | rb = {self.rb}, lb = {self.lb}, p = {None if self.parent is None else self.parent.val}"

class AVL_Tree:
    def __init__(self):
        self.root = None
    def add(self,value):
        newnode = Node(value)
        if self.root is None:
            self.root = newnode
            return
        # checked the root is empty
        if self.root.right is None and value>self.root.val:
            newnode.parent = self.root
            self.root.right = newnode
            self.root.rb = 1
            return
        if self.root.left is None and value<=self.root.val:
            newnode.parent = self.root
            self.root.left = newnode
            self.root.lb = 1
            return
        #check is there is a place to put under the root
        p = self.root
        parent = None
        while p is not None:
            parent = p
            if value > p.val:
                p = p.right
            else:
                p = p.left
        # found the place to insert
        if value>parent.val:
            parent.right = newnode
        else:
            parent.left = newnode
        newnode.parent = parent
        # inserted
        print(f'({newnode}) is added to ({parent})')
        print('Balancing...')
        self.balancetree(newnode)
    def balancetree(self,node):
        # adding lb and rb to the tree
        while node is not None:
            print(f'Currently at: {node}')
            parent = node.parent
            if parent is None:
                break
            if node.val>parent.val:
                parent.rb += 1
            else:
                parent.lb += 1
            # finished incrementing
            balance = parent.rb - parent.lb
            # trying the RR and RL
            if balance == 2:
                if 1>=node.rb-node.lb>=0:
                    self.RR(parent)
                else:
                    self.RL(parent)
                return
            # trying the LL and LR
            if balance == -2:
                if -2<node.rb-node.lb<1:
                    self.LL(parent)
                else:
                    self.LR(parent)
                return
            node = parent
    def negbalancetree(self,node):
        # adding lb and rb to the tree
        while node is not None:
            print(f'Currently at: {node}')
            parent = node.parent
            if parent is None:
                break
            if node.val>parent.val:
                parent.rb -= 1
            else:
                parent.lb -= 1
            # finished incrementing
            balance = parent.rb - parent.lb
            # trying the RR and RL
            if balance == 2:
                if 1>=node.rb-node.lb>=0:
                    self.RR(parent)
                else:
                    self.RL(parent)
                return
            # trying the LL and LR
            if balance == -2:
                if -2<node.rb-node.lb<1:
                    self.LL(parent)
                else:
                    self.LR(parent)
                return
            node = parent
    def RR(self,node):
        print('RR-ing node', node)
        A = node
        B = node.right
        T2 = B.left
        print(f'A = {A}')
        print(f'B = {B}')
        print(f'T2 = {T2}')
        p = A.parent
        if p is None:
            self.root = B
            B.parent = None
        else:
            if B.val > p.val:
                p.right = B
                B.parent = p
            else:
                p.left = B
                B.parent = p
        if B.rb - B.lb == 1:
            A.rb = A.rb - 2
        else:
            A.rb = A.rb - 1
        B.rb -= 1
        A.parent = B
        A.right = T2
        if T2 is not None:
            T2.parent = A
        B.left = A
        print('After RR rotation:')
        print(f'Root: {self.root}')
        print(f'Right {self.root.right}')
        print(f'Left: {self.root.left}')
    def LL(self,node):
        print('LL-ing node',node)
        A = node
        B = node.left
        T2 = B.right
        print(f'A = {A}')
        print(f'B = {B}')
        print(f'T2 = {T2}')
        p = A.parent
        if p is None:
            self.root = B
            B.parent = None
        else:
            if B.val > p.val:
                p.right = B
                B.parent = p
            else:
                p.left = B
                B.parent = p
        if B.rb - B.lb == -1:
            A.lb -= 2
        else:
            A.lb -= 1
        B.lb -= 1
        A.parent = B
        A.left = T2
        if T2 is not None:
            T2.parent = A
        B.right = A
    def RL(self,node):
        print('RL ROTATION')
        self.LL(node.right)
        self.RR(node)

    def LR(self,node):
        print('LR ROTATION')
        self.RR(node.left)
        self.LL(node)

    def inorder(self):
        self.inorderPrint(self.root)
        print()
    
    def postorder(self):
        self.postorderPrint(self.root)
        print()

    def preorder(self):
        self.preorderPrint(self.root)
        print()

    def inorderPrint(self,currnode):
        if currnode is None:
            return
        self.inorderPrint(currnode.left)
        print(currnode.val,end=' ')
        self.inorderPrint(currnode.right)
    
    def preorderPrint(self,currnode):
        if currnode is None:
            return
        print(currnode.val,end=' ')
        self.preorderPrint(currnode.left)
        self.preorderPrint(currnode.right)
    
    def postorderPrint(self,currnode):
        if currnode is None:
            return
        self.postorderPrint(currnode.left)
        self.postorderPrint(currnode.right)
        print(currnode.val,end=' ')
    def delete(self,value):
        if self.root is None:
            return
        if self.root.val == value:
            if self.root.right is None and self.root.left is None:
                self.__init__()
                return
            if self.root.right is None:
                # nothing in the right, so go left
                # find the rightmost left
                p = self.root.left
                follow = self.root
                while p is not None:
                    follow = p
                    p = p.right
                self.root.val = follow.val
                parent = follow.parent
                if follow.val > parent.val:
                    parent.right = p
                else:
                    parent.left = p
                if p is not None:
                    p.parent = parent
                self.negbalancetree(p)
                return
            else:
                p = self.root.right
                follow = self.root
                while p is not None:
                    follow = p
                    p = p.left
                self.root.val = follow.val
                parent = follow.parent
                if follow.val > parent.val:
                    parent.right = p
                else:
                    parent.left = p
                if p is not None:
                    p.parent = parent
                self.negbalancetree(p)
                return
        else:
            # go until found the value or reached the end
            p = self.root
            while True:
                follow = p
                if value>p.val:
                    p = p.right
                elif value<p.val:
                    p = p.left
                else:
                    node_to_delete = p
                    if node_to_delete.right is None and node_to_delete.left is None:
                        parent = node_to_delete.parent
                        if parent.right == node_to_delete:
                            parent.right = None
                        else:
                            parent.left = None
                        return
                    if node_to_delete.right is None:
                        p = node_to_delete.left
                        follow = node_to_delete
                        while p is not None:
                            follow = p
                            p = p.right
                        node_to_delete.val = follow.val
                        parent = follow.parent
                        if follow.val > parent.val:
                            parent.right = p
                        else:
                            parent.left = p
                        if p is not None:
                            p.parent = parent
                        self.negbalancetree(p)
                        return
                    else:
                        p = node_to_delete.right
                        follow = node_to_delete
                        while p is not None:
                            follow = p
                            p = p.left
                        node_to_delete.val = follow.val
                        parent = follow.parent
                        if follow.val > parent.val:
                            parent.right = p
                        else:
                            parent.left = p
                        if p is not None:
                            p.parent = parent
                        self.negbalancetree(p)
                        return
                if p is None:
                    return


nums = [1,3,2,4,56,3,5,4,-99,4,6,3,-11]
mytree = AVL_Tree()
mytree.inorder()
for i in nums:
    print(f'Adding {i}.....')
    mytree.add(i)
    mytree.inorder() #LSR
    mytree.preorder() #SLR
    mytree.postorder() #LRS
    print('----------------------------------------------')
while True:
    print('What do you want to delete?')
    num = input('Put your number here: ')
    mytree.delete(int(num))
    mytree.inorder() #LSR
    mytree.preorder() #SLR
    mytree.postorder() #LRS

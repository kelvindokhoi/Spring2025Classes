# BST (Binary Search Tree)

class Node():
    def __init__(self,v):
        self.v = v
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None
    def inserHelper(self,node,newnode):
        if node is None:
            return newnode
        if newnode.v <= node.v:
            node.left = self.inserHelper(node.left,newnode)
        else:
            node.right = self.inserHelper(node.right,newnode)
        return node
    def insert(self,v):
        newnode = Node(v)
        self.root = self.inserHelper(self.root,newnode)

    def inorderPrint(self,currnode):
        if currnode is None:
            return
        self.inorderPrint(currnode.left)
        print(currnode.v,end=' ')
        self.inorderPrint(currnode.right)
    
    def preorderPrint(self,currnode):
        if currnode is None:
            return
        print(currnode.v,end=' ')
        self.preorderPrint(currnode.left)
        self.preorderPrint(currnode.right)
    
    def postorderPrint(self,currnode):
        if currnode is None:
            return
        self.postorderPrint(currnode.left)
        self.postorderPrint(currnode.right)
        print(currnode.v,end=' ')

    def inorder(self):
        self.inorderPrint(self.root)
        print()
    
    def postorder(self):
        self.postorderPrint(self.root)
        print()

    def preorder(self):
        self.preorderPrint(self.root)
        print()
    
    def deleteHelper(self,node,camefrom,direction,v):
        if node is None:
            return
        if node.v == v:
            if node.right is None and node == self.root:
                self.root = node.left
            if node.right is None and node.left is None:
                if direction == 'left':
                    node.right = None
                else:
                    node.left = None
            elif node.right is None:
                camefrom.left = node.left
            else:
                nodetopurge = node
                node = node.right
                follow = node
                while follow.left is not None:
                    node = node.left
                    follow = node
                nodetopurge.v = node.v
                follow.left = node.right
        elif v < node.v:
            self.deleteHelper(node.left,node,'left',v)
        else:
            self.deleteHelper(node.right,node,'right',v)
    def deleteVal(self,v):
        self.deleteHelper(self.root,None,'',v)


# myprint = [6,8,18,90,4,-5,13,22,7,0,-99]
myprint = [*range(10)]

bst = BST()
for i in myprint:
    bst.insert(i)
bst.inorder()
while True:
    bst.deleteVal(int(input()))
    bst.inorder()
    print('--------------')
    bst.preorder()
    print('--------------')
    bst.postorder()

RED=0
BLACK=1

class RBTNode(object):
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
        self.parent=None
        self.color=RED


class RBTree(object):
    def __init__(self):
        self.root=None

    def search(self,node,key):
        while node:
            if key==node.val:
                return node
            if key<node.val:
                node=node.left
            else: node=node.right
        return None


    def min(self,node):
        while node.left!=None:
            node=node.left
        return node

    def max(self,node):
        while node.right!=None:
            node=node.right
        return node

    def successor(self,node):
        if node.right!=None:
            return self.min(node.right)
        tempNode=node.parent
        while tempNode!=None and node==tempNode.right:
            node=tempNode
            tempNode=node.parent
        return tempNode

    def predecessor(self,node):
        if node.left!=None:
            return self.max(node.left)
        tempNode=node.parent
        while tempNode!=None and node==tempNode.left:
            node=tempNode
            tempNode=node.parent
        return tempNode

    def insert(self,node):
        y=None
        x=self.root
        while x!=None:
            y=x
            if node.val<x.val:
                x=x.left
            else: x=x.right

        node.parent=y
        if y==None:
            self.root=node
        elif node.val<y.val:
            y.left=node
        else: y.right=node
        self.RBInsertFixUp(node)

    def RBInsertFixUp(self,z):
        while z.parent.collor==RED:
            if z.parent==z.parent.parent.left:
                y=z.parent.parent.right
                if y.color==RED:
                    z.parent.color=BLACK
                    y.color=BLACK
                    z.parent.parent=RED
                    z=z.parent.parent
            elif z==z.parent.right:
                z=z.parent
                self.leftRotation(z)
            z.parent.color=BLACK
            z.parent.parent.color=RED
            self.rightRotation(z.parent.parent)

        self.root.color=BLACK

    def leftRotation(self,x):
        y=x.right
        x.right=y.left
       # if


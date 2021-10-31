import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL





    def inorder(root):
        if root:
            self.inorder(root.left)
            sys.stdout.write(root.data + " ")
            self.inorder(root.right)




    def leftrotation(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y 
        elif x is x.parent.left:
            x.parent.left = y 
        else:
            x.parent.right = y
        y.left = x
        x.parent = y



     def rightrotation(self, y):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


    def inserfixup(self, node):
        while node.parent.color = 1 : # for red
            if node.parent == node.parent.parent.left:
                #node.parent is left child 
                y = node.parent.parent.right 
                if y.color == 1: #case 1
                    node.parent.parent = 0
                    y.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent


                else: # case 2 
                    if node == node.parent.right:
                        node = node.parent
                        self.leftrotation(node)

                        #case3
                        node.parent.color = 0
                        node.parent.parent = 1
                        self.rightrotation(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == 1: #case 1
                    node.parent.parent = 0
                    y.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent


                else: # case 2 
                    if node == node.parent.right:
                        node = node.parent
                        self.rightrotation(node)

                        #case3
                        node.parent.color = 0
                        node.parent.parent = 1
                        self.leftrotation(node.parent.parent)

        self.root.color = 0 



    def insertion(self,data):
        node = Node(data)
        node.parent = None
        node.data = data
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1
        y = None
        temp = self.root




        while temp is not self.TNULL:
            y = temp 

            if node.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right 
        
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 0 

        self.inserfixup(node)


    def rb_trasplant(self, u, node):
        if u.parent = self.TNULL:
            self.root = node

        elif u == u.parent.left:
            u.parent.left = node
        else:
            u.parent.right = node

        node.parent = u.parent











    

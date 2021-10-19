class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def successor(root, node):
    if node.right is not None:
        return minimum(node.right)
    
    p = temp.parent
    while(p is not None and node == p.right):
        node = p
        p = p.parent
    return p
    
def predecessor(root, node):
    if node.left is not None:
        return maximum(node.left)
        
    p = temp.parent
    while(p is not None and node == p.left):
        node = p
        p = p.parent
    return p 

def inorder(root):
    if root is None:
        return 
    else:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

"""def preorder(root):
    if root is None:
        return 
    else:
        print(root.data)
        preorder(root.left)
        preorder(root.right)



def postorder(root):
    if root is None:
        return 
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
"""

def minimum(root):
    current = root
    while(current.left is not None):
        current = current.left
    return current

def maximum(root):
    curr = root
    while(curr.right is not None):
        curr = curr.right
    return curr
    

def insert(node, data):
    if node is  None:
        return Node(data)
    
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right= temp
            temp.parent = node

        return node







root = None
root = insert(root, 20)
root = insert(root, 8)
root = insert(root, 22)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 10)
root = insert(root, 14) 
temp = root.left.right

succ = successor(root, temp)
pred = predecessor(root, temp)

if succ is not None:
    print( " the number after % d is % d"
    %(temp.data, succ.data))
    
if pred is not None:
    print("the number before % d is % d"
    %(temp.data, pred.data))

"""print ("Preorder traversal of binary tree is")
preorder(root)

print ("Postorder traversal of binary tree is")
postorder(root)


print("the minimum is",minimum(root))"""



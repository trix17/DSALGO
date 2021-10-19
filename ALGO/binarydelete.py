class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




#insertion 
def insert(node, data):
    if node is None:
        return Node(data)

    if data <= node.data:
        node.left = insert(node.left, data)

    else:
        node.right = insert(node.right, data)
    return node


# Deletion 
def delete(root, data):
#places to search for data/key
    if root is None:
        return root
    if data < root.data:
        root.left  = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)


#if node has one child
    else:
        if root.left is None:
            temp = root.right 
            root = None
            return temp 
        
        elif root.right is None:
            temp = root.left 
            root = None
            return temp 

#if root has two children 
        else:
            temp = minimum(root.right)
            root.data = temp.data   # copy temp value to root
            root.right = delete(root.right, temp.data)
            
    
    return root
    






def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def minimum(root):
    while (root.left is not None):
        root = root.left
    return root 


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)



print ("Inorder traversal of the given tree")
inorder(root)
 
print ("\nDelete 20")
root = delete(root, 20)
print ("Inorder traversal of the modified tree")
inorder(root)
 
print ("\nDelete 30")
root = delete(root, 30)
print ("Inorder traversal of the modified tree")
inorder(root)
 
print ("\nDelete 50")
root = delete(root, 50)
print ("Inorder traversal of the modified tree")
inorder(root)
 
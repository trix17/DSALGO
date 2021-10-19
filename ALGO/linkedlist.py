class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None 




# Function to add up front 
    def add(self, data): 
        newnode = Node(data)

        #self.head = newnode
        #newnode = newnode.next

        newnode.next = self.head
        self.head = newnode
    # Function to add after prev_node 
    def middle(self, prev_node,data):
        newnode = Node(data)
        newnode.next = prev_node.next 
        prev_node.next = newnode
        
    #Funcntion to add it at the end 
    def end(self, data):
        newnode = Node(data)
        #If the Linked List is empty, then make the
          #new node as head
        if self.head is None:
            return
        

        #Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        #Change the next of last node
        last.next = newnode
        





    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ =="__main__":
    llist = linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    

    
    llist.head.next = second
    second.next = third
    third.next = fourth 

    llist.end(111)
    llist.middle(second,10)
    llist.add(7)
    llist.printlist()
    

         


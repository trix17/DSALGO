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
#1--> 2-->

    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next
            
        self.head = prev




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
    
    

    print("The list before reverse it")
    llist.add(7)
    llist.add(6)
    llist.add(5)
    llist.printlist()


    print("The list afte reverse it:")
    llist.reverse()
    llist.printlist()
    

         


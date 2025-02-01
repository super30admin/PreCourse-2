# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data =data
        self.nex=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None

    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head= new_node

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        sp = self.head
        fp = self.head
        while fp and fp.next:
            sp= sp.next
            fp= fp.next.next
        if sp:
            print("middle ele is ",sp.data)
        else:
            print("List is Empty")


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

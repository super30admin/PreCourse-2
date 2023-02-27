# Node class
class Node:

    # Function to initialise the node object  
    def __init__(self, data, next):  
        self.data= data
        self.next= next

class LinkedList: 
  
    def __init__(self): 
        self.head= None
  
    def push(self, new_data): 
        if self.head is None:
            self.head= Node(new_data, None)

        self.new_node= Node(data= new_data, next= None)
        node_loc = self.head
        while node_loc.next != None:
            node_loc = node_loc.next
        node_loc.next = self.new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        i = 1
        node_loc = self.head 
        while  node_loc.next is not None: 
            node_loc = node_loc.next 
            i += 1 

        size = i + 1 
        mid = (size + 1)//2
        node_loc = self.head
        while mid > 1: 
            node_loc = node_loc.next
            mid -= 1 
        print(node_loc.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
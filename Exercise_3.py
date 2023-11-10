# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
class LinkedList: 
  
    def __init__(self): 
        self.head  = None        
  
    def push(self, new_data):
        node = Node(new_data) 
        if self.head == None:
            self.head = node
        else:    
            node.next = self.head
            self.head = node
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        pt1  = self.head
        pt2 = self.head
        while pt2.next != None:
            pt2 = pt2.next.next
            pt1= pt1.next
        print(pt1.data)   
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

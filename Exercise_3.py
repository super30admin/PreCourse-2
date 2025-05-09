# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None  
        
class LinkedList: 
  
    def __init__(self):
        self.head = None 
        
  
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        x = self.head #x here moves one step at a time
        y = self.head #y moves two steps at a time
        while y and y.next: #Two pointers
            x = x.next
            y = y.next.next
        if x:
            print("Middle Element is:", x.data) #When y reaches the end x is at the middle
        else:
            print("Empty List")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

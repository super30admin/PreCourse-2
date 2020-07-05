# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
    	self.data = data
    	self.next = None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head = Node(0)
        self.end = self.head
  
    def push(self, new_data):
    	self.end.next = Node(new_data)
    	self.end = self.end.next 
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
    	p1 = p2 = self.head
    	while p2 and p2.next:
    		p1 = p1.next
    		p2 = p2.next.next
    	print(p1.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

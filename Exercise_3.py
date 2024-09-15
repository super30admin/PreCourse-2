# Node class  
class Node:  
    
    # Function to initialise the node object  
    def __init__(self, data):
        self.data=data
        self.next=None

        
class LinkedList: 
  
    def __init__(self):
        self.head=None 
        
  
    def push(self, new_data):
        n1 = Node(new_data) 
        n1.next = None
        self.head=n1
        
    
    def printMiddle(self):
        p1 = self.head
        p2 = self.head
        while p2.next:
            p1 = p1.next
            p2 = p2.next.next
            
        return (p2.data)
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()

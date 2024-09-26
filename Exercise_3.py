# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.key=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
        
  
    def push(self, new_data): 
        new_Node=Node(new_data)
        new_Node.next=self.head
        self.head=new_Node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=slow.next.next
        print(slow.key)





# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 


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
        New_node=Node(new_data)
        New_node.next=self.head
        self.head=New_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):  
        fast=self.head #First initially slow and fast points to head
        slow=self.head
        while fast and fast.next != None: #For odd length and even length 
            slow=slow.next #Slow pointer moves one step
            fast=fast.next.next  #Fast pointer moves 2 steps
        print(slow.data) #As fast pointer reaches the end that means slow pointer is at middle position!

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

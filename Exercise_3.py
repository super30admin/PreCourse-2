# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data  
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
  
    def push(self, new_data):
            t=Node(new_data)
            t.next=self.head
            self.head=t
    
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head==None:
            print("The list is empty")
            return
        
        slow=self.head
        fast=self.head.next
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        print(slow.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3)
list1.push(1)
list1.printMiddle()
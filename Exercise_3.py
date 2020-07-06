# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data,next=None):
        self.data=data
        self.next=next
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.len = 0
  
    def push(self, new_data): 
        self.head =Node(new_data,self.head)
        self.len += 1
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        ptr=self.head
        for i in range(self.len//2):
            ptr=ptr.next
        print(ptr.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

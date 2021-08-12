# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
        self.count=0
        
  
    def push(self, new_data): 
        self.count=self.count+1
        if self.head==None:
            self.head=Node(new_data)
        else:
            current=self.head
            while(current.next):
                
                current=current.next
            current.next=Node(new_data)
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        i=0
        current=self.head
        while(i<self.count//2):
            i=i+1
            
            current=current.next
        print("The middle term is",current.data)
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 

list1.printMiddle() 

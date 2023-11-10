# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None,next=None):  
        self.data=data
        self.next=next

class LinkedList: 
  
    def __init__(self): 
        self.head=Node(0)
        
  
    def push(self, new_data): 
        if self.head.next is None:
            self.head.next=Node(new_data)
            return 

        ptr=self.head
        
        while ptr.next is not None:
            ptr=ptr.next
        ptr.next=Node(new_data)
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow=self.head.next
        fast=self.head.next

        while fast.next is not None and fast is not None:
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

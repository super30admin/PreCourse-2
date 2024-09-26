# Node class
# Here we use two pointers. One pointer move one by one whereas another pointer moves by two \. So when the later
#reaches end, the slow pointer reaches the middle index, hence we return the element present at middle index.
class Node:
  
    # Function to initialise the node object
    def __init__(self, data):
        self.data=data
        self.next=None
        
class LinkedList:
  
    def __init__(self):
        self.head=None
        
  
    def push(self, new_data):
        if self.head is None:
            self.head=Node(new_data)
            
        else:
            newNode=Node(new_data)
            newNode.next=self.head
            self.head=newNode
            
        
  
    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        slowPtr=self.head
        fastPtr=self.head
        
        if self.head is not None:
            while(fastPtr is not None and fastPtr.next is not None):
                slowPtr=slowPtr.next
                fastPtr=fastPtr.next.next
                
            print("The middel element is: ", slowPtr.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

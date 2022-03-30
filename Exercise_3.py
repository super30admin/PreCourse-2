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
        newnode = Node(new_data)
        newnode.next = self.head
        self.head = newnode
       
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        start = self.head
        last = self.head
        #When the fast pointer reaches end slow pointer will reach middle of the linked list.
        if self.head is not None:
            while (last is not None and last.next is not None):
                last = last.next.next
                start = start.next
            print("The middle element is: ", start.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

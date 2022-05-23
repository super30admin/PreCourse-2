# Author: Vineet Khanna

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
        node1 = Node(new_data)
        node1.next = self.head
        self.head = node1
         
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        p = self.head
        count = 0
        
        while p:
            count += 1
            p = p.next

        
        new_count = count//2

        p = self.head
        for i in range(new_count):
            p = p.next

        print(p.data)




# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 


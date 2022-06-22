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
        new_Node = Node(new_data)
        if not self.head:
            self.head = new_Node
            return
        
        current = self.head
        while (current.next):
            current = current.next
        
        current.next = new_Node

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        print(arr[len(arr)//2])
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

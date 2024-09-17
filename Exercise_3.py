# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        self.tail = None 
        
  
    def push(self, new_data): 
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        temp = self.head
        size = 0
        while temp is not None:
            temp = temp.next
            size += 1
        temp = self.head
        for i in range(size//2):
            temp = temp.next
        print(temp.data)
             

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

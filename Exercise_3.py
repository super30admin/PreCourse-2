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
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def getLength(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length
    
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        length = self.getLength()
        mid_index = length // 2
        current = self.head
        while mid_index > 0:
            current = current.next
            mid_index -= 1
        if current:
            print(f"The middle element is: {current.data}")
        else:
            print("The linked list is empty.")
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

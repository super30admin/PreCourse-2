# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None 
        
class LinkedList: 
  
    def __init__(self): 
        self.root= None
  
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.root
        self.root = new_node
        
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        #Initializing slow and fast pointer moving one and two steps at a time
        slow_ptr = self.root
        fast_ptr = self.root

        if self.root is not None:
            while(fast_ptr and fast_ptr.next):
                slow_ptr = slow_ptr.next 
                fast_ptr = fast_ptr.next.next
            
            print("The middle element is:",slow_ptr.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

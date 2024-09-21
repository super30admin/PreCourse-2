# Node class  
class Node:  
    # Function to initialize the node object  
    def __init__(self, data):  
        self.data = data  # Assign data
        self.next = None  # Initialize next as None

# LinkedList class  
class LinkedList: 
  
    def __init__(self): 
        self.head = None  # Initialize head as None
        
    # Method to add a new node at the front of the list
    def push(self, new_data): 
        new_node = Node(new_data)  # Create a new node
        new_node.next = self.head  # Make the new node point to the head
        self.head = new_node       # Move the head to point to the new node
  
    # Function to get the middle of the linked list
    def printMiddle(self): 
        slow_ptr = self.head  # Initialize slow pointer
        fast_ptr = self.head  # Initialize fast pointer
        
        if self.head is not None:
            while fast_ptr is not None and fast_ptr.next is not None:
                slow_ptr = slow_ptr.next          # Move slow_ptr by one
                fast_ptr = fast_ptr.next.next     # Move fast_ptr by two
            
            print(f"The middle element is {slow_ptr.data}")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()

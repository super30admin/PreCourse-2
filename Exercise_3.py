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
        # Allocate the Node & put in the data
        new_node = Node(new_data)
        
        # Make next of new Node as head
        new_node.next = self.head
        
        # Move the head to point to new Node
        self.head = new_node
  
    # Function to get the middle of  
    # the linked list
    # Time Complexity: O(n) - Only one traversal of the linked list is needed
    # Space Complexity: O(1) - Only two pointer variables are used regardless of list size 
    def printMiddle(self): 
        # Initialize two pointers, one will go one step a time (slow)
        # Another will go two steps a time (fast)
        slow_ptr = self.head
        fast_ptr = self.head
        
        # Move fast_ptr by 2 and slow_ptr by 1
        # Eventually, when fast_ptr reaches the end,
        # slow_ptr will be at the middle
        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            
            # slow_ptr is now at the middle
            print("The middle element is: ", slow_ptr.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

# Time Complexity: O(n)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode: Couldn't find this problem on Leetcode
# Any problem you faced while coding this: No

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None  # Initialize head as None
  
    def push(self, new_data): 
        # Create a new Node
        new_node = Node(new_data)
        
        # Make next of new Node as head
        new_node.next = self.head
        
        # Move the head to point to new Node
        self.head = new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # Initialize two pointers, one will move one step at a time
        # and other will move two steps at a time
        slow_ptr = self.head
        fast_ptr = self.head
        
        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
                
            print("The middle element is:", slow_ptr.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

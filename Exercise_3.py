# Time Complexity: O(n)
# Space Complexity: O(1)

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data=data
        self.next=None 
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None # head as null
    def push(self, new_data): 
        new_node=Node(new_data) # Create a new node with data
        new_node.next=self.head # Make next of new node as head
        self.head=new_node # Move the head to point to new node 
    def printMiddle(self):
        slow_ptr = self.head  # Moving only 1 step at a time.
        fast_ptr = self.head  # Moving 2 step at a time.

        if self.head is not None:
            while fast_ptr is not None and fast_ptr.next is not None:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            print("The middle element is:", slow_ptr.data) 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

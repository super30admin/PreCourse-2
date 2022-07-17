# Time Complexity : O(n), as it takes us n/2 time to reach the middle element
# Space Complexity : No extra space is needed, only O(n) for the linked list
# Did this code successfully run on Leetcode : Code ran successfully.
# Any problem you faced while coding this : No problems

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data # Initialize Node with data value given as parameter
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None 
        
  
    def push(self, new_data):
        # Assuming that we are push element to the front like in stack and not like append (which we add to the end)
        new_node = Node(new_data) # Create new node with value new_data
        new_node.next = self.head # Make the next element of the new node as our current head
        self.head = new_node # Make head point to our current new node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if not self.head:
            return # There can be no middle element if the linked list is empty
        slow = self.head # Initializing a slow ptr starting at head
        fast = self.head # Initializing a fast ptr starting at head 
        while(fast and fast.next): # Loop stops when fast reaches the end and becomes None and slow will point to the middle element
            slow = slow.next # Move slow to the next element
            fast = fast.next.next # Move fast to the second next element
        print(slow.data) #Print the value at slow which is the middle element value
        return
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2)
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

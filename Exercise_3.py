# Time Complexity : O(N)
# Space Complexity :O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : I couldnt optimize it better.


# Node class  
class Node:  

    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data  # Store the node's data
        self.next = None  # Initialize next as None

# LinkedList class  
class LinkedList: 

    def __init__(self): 
        self.head = None  # Initialize the head of the list
        
    def push(self, new_data): 

        # Insert a new node at the beginning of the list
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    # Function to get the middle of the linked list (my approach)
    def printMiddle(self): 
        # First pass: Count the total number of nodes in the list
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        
        # Calculate the middle index
        mid_index = count // 2
        
        # Second pass: Traverse to the middle node
        current = self.head
        for _ in range(mid_index):
            current = current.next
        
        # Print the middle element's data
        print("Middle element is:", current.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()

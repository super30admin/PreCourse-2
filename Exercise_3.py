# Time Complexity : O(n)
# Space Complexity : o(1)
# Did this code successfully run on Leetcode : No 
# Any problem you faced while coding this : No

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data # assign data 
        self.next = None # Initialize the next null
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None  # Initialize head as None
  
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        ptr1 = self.head # Start both pointers at the head
        ptr2 = self.head

        if self.head is not None:
            while ptr2 is not None and ptr2.next is not None:
                ptr1 = ptr1.next # Move ptr1 by one node
                ptr2 = ptr2.next.next # Move ptr2 by two nodes

            print("The middle element is: ", ptr1.data)

# Driver code 
list1 = LinkedList() 
# list1.push(7)
list1.push(8)
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle() 

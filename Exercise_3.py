# // Time Complexity : O(n) where n is the number of elements added in the list, TC for checking middle of the list is O(lg n)
  # // Space Complexity : O(n) where n is the number of elements added in the list 
  # // Did this code successfully run on Leetcode : yes
  # // Any problem you faced while coding this : none

  # // Your code here along with comments explaining your approach

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data 
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        # taking a dummy node for ease of traversal 
        # of even and odd len lists
        self.head = Node(0)
        self.end = self.head
  
    def push(self, new_data): 
        
        # adding node at the end 
        # making end point to the new node
        node = Node(new_data)
        self.end.next = node
        self.end = self.end.next
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # using 2 ptr approach
        # slow ptr moves at half the pace of fast ptr
        ptr1 = ptr2 = self.head

        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        
        if ptr1:
            print(ptr1.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
# list1.push(1) 
list1.printMiddle() 

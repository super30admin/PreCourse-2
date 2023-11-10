# Time complexity = O(n) --> it's actually n//2 as the fast pointer traverses two nodes at a time and our search ends when
# the fast pointer reaches the last node.
# Space complexity = O(n) - to store the input array.

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
        # Insert at the beginning
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

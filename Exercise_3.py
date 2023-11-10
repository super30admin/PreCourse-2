# Time complexity: O(n)
# space complexity: O(1) 
class Node:
   
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as none
   
   
# Linked List class contains a Node object
class LinkedList:
   
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
 
    # Function to get middle of linkedlist.
    def printMiddle(self):
        slow = self.head
        fast = self.head
 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            return slow.data
 
# Code execution starts here
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(3)
list1.push(2)
list1.push(1)
list1.printMiddle()
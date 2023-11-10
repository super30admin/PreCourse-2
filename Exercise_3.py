'''
Time Complexity: O(n)
Space Complexity: O(n)
Problems: to find a solution that 
finds the middle of the list in just
one itteration.
'''

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
        node = Node(new_data)
        node.next = self.head
        self.head = node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        fast_pointer = self.head
        slow_pointer = self.head
        if self.head != None or self.head.next != None:
            while fast_pointer != None and fast_pointer.next != None:
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
        print(slow_pointer.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(0)
list1.push(-1)
list1.printMiddle() 

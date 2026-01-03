# Node class 
"""
we use slow pointer and fast pointer to find the mid of the linkedlist 
once the fast pointer reaches the tail then the slow pointer will be at the middle
"""
class Node:
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None 

        
class LinkedList:
    def __init__(self): 
        self.head = None
        self.tail = None
  
    def push(self, new_data):
        temp = Node(new_data)

        if self.head is None:
            self.head = temp
            self.tail = temp
            return
        
        self.tail.next = temp
        self.tail = temp
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):

        if self.head is None:
            return "List is empty"
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.data)
        return slow

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

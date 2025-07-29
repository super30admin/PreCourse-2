# Time complexity - O(n)
# Space complexity - O(1)

# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data, next = None):  
        self.data = data
        self.next = next
        
class LinkedList: 
    def __init__(self): 
        self.start = None
    
    # initializing new node to add to linked list
    def push(self, new_data): 
        new = Node(new_data)
        new.next = self.start
        self.start = new
  
    # Function to get the middle of the linked list 
    # using slow and fast pointer to traverse the list, since fast travels at 2 times slow pointer, when fast reaches end of list, slow will reach the middle
    def printMiddle(self): 
        slow = self.start
        fast = self.start
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        if slow: print("Middle element is:", slow.data)
        
        
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

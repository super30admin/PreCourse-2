# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        new_node = Node(new_data)  
        new_node.next = self.head  
        self.head = new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
         # Initialize two pointers, one will go one step a time (slow), another two at a time (fast)
        slow = self.head
        fast = self.head
  
        # Iterate till fast's next is null (fast reaches end)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
          
        # return the slow's data, which would be the middle element.
        print("The middle element is ", slow.data)
        
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

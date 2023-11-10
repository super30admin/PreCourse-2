# Time complexity: O(n)
# Space complexity:O(1) 
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null  
        
class LinkedList: 
    
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to insert a new node at the beginning  
    def push(self, new_data):  
        new_node = Node(new_data)  
        new_node.next = self.head  
        self.head = new_node
  
 
    # Function that returns middle.
    def printMiddle(self):

        # Initialize two pointers
        slow = self.head  # go one step a time (slow)
        fast = self.head  # go two at a time (fast)
  
        # Iterate till fast's next is null 
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
list1.push(6)
list1.push(0)
list1.printMiddle() 

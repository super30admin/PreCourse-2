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
        f = self.head
        s = self.head
        # for even nodes, if the first middle node is to be returned
        """
        while f.next:
            f = f.next
            if f.next:
                f = f.next
                s = s.next
        """
        # if the second middle node is to be returned:
        while f and f.next:
            s = s.next
            f = f.next.next
        if not s:
            print ("Empty List")
        else:
            print ("Middle element = ", s.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle() 
"""
n = number of elements in the array
Space Complexity: O(1) 

Time Complexity:
O(n) , one pass.
"""
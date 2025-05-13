# Node class  
"""
Time Complexity: 
init: O(1)
push: O(1)

PrintMiddle: O(n)


Space Complexity:

init: O(1)
push: O(1) per call, total list space is O(n)
printMiddle: O(1)

"""
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None):
        self.data = data 
        self.next = None

class LinkedList: 
  
    def __init__(self):
        self.head = None
        self.tail = None
  
    def push(self, new_data): 
        new_node = Node(new_data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            prev = self.tail 
            prev.next = new_node 
            self.tail = new_node

        
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head is None:
            raise ValueError("List is empty")

        slow = fast = self.head 
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        print(slow.data)
        return 
            
            
         
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

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
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while(curr_node.next is not None):
                curr_node = curr_node.next
            curr_node.next = new_node
        
  
    # Function to get the middle of the linked list 
    def printMiddle(self):
        fast_node = slow_node = self.head
        while(fast_node is not None and fast_node.next is not None):
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        print(slow_node.data)
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

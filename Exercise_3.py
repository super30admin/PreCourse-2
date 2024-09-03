# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.val = data
        self.next = None 
class LinkedList: 
    def __init__(self): 
        self.head = None
    def push(self, new_data): 
        new_node = Node(new_data)
        if self.head!= None:
            new_node.next = self.head.next
            self.head.next = new_node
        else:
            self.head = new_node

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head
        fast = self.head
    
        while fast!= None and fast.next!= None:
            fast = fast.next.next
            slow = slow.next
        return slow.val
        
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
middle = list1.printMiddle() 
print(middle)

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self. data = None
        self. next = None
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.last_node = None
    def push(self, new_data): 
        if self.head is None:
            self.head = Node(new_data)
            self.last_node = self.head
        else:
            self.last_node.next  = Node(new_data)
            self.last_node = self.last_node.next 
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
     ## two pointer 
     first = self.head
     second = self.head

     if self.head is None:
         if first is not None and first.next is not None:
             first = first.next.next
             second = second.next

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        
class LinkedList: 
  
    def __init__(self): 
        
  
    def push(self, new_data): 
        new_node = Node(new_data)  
        new_node.next = self.head  
        self.head = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        p1 = self.head
        p2 = self.head

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        return print(p2.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

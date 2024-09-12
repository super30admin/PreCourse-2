# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.size = 0
  
    def push(self, new_data):
        new_node = Node(new_data)
        if self.size == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        curr = self.head
        after = self.head
        while (after is not None and after.next is not None):
            after = after.next.next
            curr = curr.next
        print(curr.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3)
list1.push(1) 
list1.printMiddle() 

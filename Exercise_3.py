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
        # push a new node into the linked list.  Make sure to re-assign head 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        runner = self.head
        walker = self.head

        while runner.next and runner:
            runner = runner.next.next
            walker = walker.next

        print("Middle value is {}".format(walker.data))

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

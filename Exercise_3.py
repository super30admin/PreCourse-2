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
        if self.head == None:
            self.head = Node(new_data)
        else:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node 
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow, fast = self.head, self.head
        if self.head != None:
            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
            return slow.data 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

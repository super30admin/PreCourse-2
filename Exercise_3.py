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
        pt1 = self.head
        pt2 = self.head
      
        while pt1 and pt1.next:
            pt1 = pt1.next.next
            pt2 = pt2.next
          
        print(pt2.data)
      

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

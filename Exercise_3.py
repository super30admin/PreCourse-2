# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
      self.data=data
      self.next=None
        
class LinkedList: 
  
    def __init__(self): 
       self.head=None
  
    def push(self, new_data): 
      node=Node(new_data)
      node.next=self.head
      self.head=node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
      result=0
      mid_node=self.head

      while self.head is not None:
        if result%2 !=0:
            mid_node=mid_node.next
        self.head=self.head.next
        result+=1

      if mid_node is not None:
        print mid_node.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

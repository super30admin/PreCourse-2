# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
class LinkedList: 
  
    def __init__(self): 
      self.head = None
      self.count = 0
  
    def push(self, data): 
      if self.head == None:
        self.head = Node(data)
        
      temp = Node(data)
      temp.next = self.head
      self.head = temp
      self.count += 1
      
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
      mid = self.count // 2
      if self.head is None:
        return None
      curr = self.head
      for i in range(mid):
        curr = curr.next
        
      return curr.data
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

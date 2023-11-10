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
      #creat new node
      nn = Node(new_data)
      nn.next = self.head
      self.head = nn
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
      #using the 2 pointer approach, ptr 1 will move by one step and ptr 2 will move by 2 steps
      #scenario when ptr2 cannot move any further, ptr1 will be the mid point of the linked list
      if self.head:
        ptr1, ptr2 = self.head, self.head
        while (ptr2 is not None and ptr2.next is not None):
          ptr1 = ptr1.next
          ptr2 = ptr2.next.next
        return ptr1
      else:
        return "None"
          
        
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

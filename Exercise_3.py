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
      ##Add new node at the end
      newNode = Node(new_data)
      if(self.head):
        current = self.head
        while(current.next):
          current = current.next
        current.next = newNode
      else:
        self.head = newNode
        
      ##Add new node at the beginning
      newNode = Node(new_data) 
      newNode.next = self.head 
      self.head = newNode

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
      slow = self.head
      fast = self.head
      
      ## slow pointer goes at normal pace, fast goes two at a time
      ## once fast pointer reaches null, the node pointed at by slow is the middle of Linked List
      while fast and fast.next:
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

#Time Complexity - O(n)
#Space Complexity - O(1)

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
      #push to the end of the list
      new_node = Node(new_data)
      if not self.head:
        self.head = new_node
        return
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
      slow = self.head
      fast = self.head
      while fast and fast.next:
        slow = slow.next #traverse by 1
        fast = fast.next.next #traverse by 2
      if slow:
        print("Midpoint:", slow.data)
      else:
        print("List is empty")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

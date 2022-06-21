'''
Time Complexity : O(n)
Space Complexity : O(1)
'''
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
        temp = Node(new_data)

        if self.head is None:
          self.head = temp
        else :
          curr = self.head
          while(curr.next is not None):
            curr = curr.next
          curr.next = temp
        self.size += 1
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
      present = 0
      temp = self.head
      mid = self.size//2
      # print(self.size)
      while(present<mid):
        # print(temp.data)
        temp = temp.next
        present = present +1
      return temp.data
        
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(0)
print(list1.printMiddle())

#Time Complexity :  O(n)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : no
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
      self.data=data # assign data
      self.next=None # initialize next as None
        
class LinkedList: 
  
    def __init__(self): 
      self.head=None
      
    def push(self, new_data): 

      #insert node in the beginning 
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
      fast=self.head # fast pointer moves 2 steps at a time
      slow=self.head # slow pointer moves 1 step at a time

      while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
      print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(8)
list1.push(7)
list1.push(6)
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
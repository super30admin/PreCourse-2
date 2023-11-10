# Node class  
# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# We use two pointers. The slow one advances one node at a time and the fast one advances 2 nodes at a time.
# So, when the fast node reaches the end of the linked list, the slow one will have reached the middle.
from email import header
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data=data 
        self.next=None
        
class LinkedList: 
  
    def __init__(self):
        self.head=None        
  
    def push(self, new_data):
        newNode=Node(new_data)
        if self.head==None:
            self.head=newNode
        else:
            lastnode=self.head
            while lastnode.next:
                lastnode=lastnode.next
            lastnode.next=newNode

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):

        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle()

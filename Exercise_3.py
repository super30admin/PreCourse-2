# Node class 

# Time Complexity : O(n)
# Space Complexity :O(1)
# Did this code successfully run on Leetcode? : Verified by succesfully running on code editor
# Any problem you faced while coding this : No

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data): 
        new = Node(new_data)
        new.next = self.head
        self.head = new
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        full = half = self.head
        while full.next != None:
            full = full.next.next
            half = half.next
        print("Middle of Linked List is: " +str(half.data))
        return
            

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

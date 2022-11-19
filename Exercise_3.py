# Node class  
# // Time Complexity : O(log(n))
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next  

        
class LinkedList: 
  
    def __init__(self): 
        self.head = Node(-1)
        self.dummy = self.head
        
  
    def push(self, new_data): 
        temp = Node(new_data)
        self.dummy.next = temp
        self.dummy = temp
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        fast = self.head.next
        slow = fast
        print("in")
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print( slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

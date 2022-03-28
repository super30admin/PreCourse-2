#Time Complexity : O(N)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this :

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None,next=None):  
    	self.data = data
    	self.next = next
        
class LinkedList: 
  
    def __init__(self): 

        self.head = None

  
    def push(self, new_data): 

    	node = Node(new_data,self.head)
    	self.head = node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 

        slow = fast = self.head
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


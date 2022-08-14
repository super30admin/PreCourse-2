# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Node class  

# Time Complexity : O(n) n is the number of nodes in the link list
# Space Complexity : O(1)
# Did this code successfully run on Leetcode :  Yes
# Any problem you faced while coding this :  No
class Node:  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        temp = Node(new_data)
        temp.next = self.head
        self.head = temp
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next                # slow must be in the middle when fast reaches the end of the list
            fast = fast.next.next
        print (slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
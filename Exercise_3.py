"""
// Time Complexity :  O(n), where n is the number of elements in the linked list
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : No
"""

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
        node = Node(new_data)
        if self.head==None: #if the linkedlist is empty, make the new node the head 
            self.head=node
        else:
            ptr = self.head #else iterate over the entire list to get to the end, where the next variable for the node is None
            while ptr.next:
                ptr=ptr.next
            ptr.next=node #attach the node at the last node
            
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): #approached the problem using a slow and fast pointer
        slow=fast=self.head    

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle() )

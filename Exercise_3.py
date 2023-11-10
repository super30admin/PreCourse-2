'''
// Time Complexity : O(n) for finding the middle, O(1) to insert at the beginning
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None 

We use two pointers fast and slow, we iterate fast pointer at 2x speed, slow at 1x speed.
When our fast pointer hits Null, our while loop breaks and the slow pointer will point to
middle element.
'''

# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data,next=None):
        self.data=data
        self.next=next
    
    def __str__(self):
        return str(self.data)
        
class LinkedList: 
  
    def __init__(self,root=None): 
        self.root=root
  
    def push(self, new_data): 
        new_node=Node(new_data,self.root)
        self.new_data=new_data
        self.root=new_node
    
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow=fast=self.root
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print("Middle Element is :",slow)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 


# Node class 
# Solved it by two pointer approach
# Time Complexity: O(N)
# Space complexity: O(1) 
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data=data
        self.next=None  
        
class LinkedList: 
  
    def __init__(self):
        self.head=None 
        
  #Add new node to the head of the linked list
    def push(self, new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self_head=new_node

        
  
    # Function to get the middle of  
    # the linked list 
    #return if list is empty
    # initialize slow and fats pointers at head, incremet slow by 1 and fast by 2 spaces
    # when fast reaches null, the slow must have covered the half list, so print slow.data 
    def printMiddle(self):
        if self.head==None:
            return
        slow=self.head
        fast=self.head
        while(fast.next!=None and fast.next.next!=None):
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

# Time Complexity : O(N)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes on terminal
# Any problem you faced while coding this : No

""" 
We used turtoise and hare algorithm, where one pointer moves fast and second move slow and both meet at the center
"""
# Python program for implementation of Quicksort Sort 
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
        self.node = Node(new_data)
        self.node.next = self.head
        self.head = self.node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

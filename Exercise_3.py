# Node class 
# // Time Complexity : O(N)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode :Yes
''' Any problem you faced while coding this : 
Initiated two pointers slowNode and FastNode.
slowNode incremented with 1 node and fastNode incremented with 2 nodes resp.'''

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
  '''when the fastNode reaches the end node
  slow node is at the middle of the singly linked list 
  and we have returned that value'''
    # Function to get the middle of the linked list 
    def printMiddle(self): 
        slowNode = self.head
        fastNode = self.head
        while fastNode and fastNode.next:
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        print(slowNode.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

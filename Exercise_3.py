"""Time Complexity : O(n)
Space Complexity : O()
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
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
    # If head is null then we need to handle that
    # if not then we add a node at the beginning 
    def push(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
        else:
            newNode = Node(new_data)
            newNode.next = self.head
            self.head = newNode
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # We initialize two pointer both at the head node
        firstPoint = self.head
        twoPoint = self.head
        # We iterate through the list with these two pointers
        # one will move one step and another will move two step
        # so when the two step pointer reaches the end the one step
        # would have reached the middle of the linked list
        while twoPoint != None and twoPoint.next != None:
            firstPoint = firstPoint.next
            twoPoint = twoPoint.next.next
        print("The middle point is:", firstPoint.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

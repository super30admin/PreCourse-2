# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = Node(None)

    def push(self, new_data):
        if not self.head.data:
            self.head.data = new_data
        else:
            self.newNode = Node(new_data)
            self.newNode.next = self.head
            self.head = self.newNode
   
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        self.fast = self.slow = self.head

        while self.fast and self.fast.next:
            self.slow = self.slow.next
            self.fast = self.fast.next.next

        print(self.slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

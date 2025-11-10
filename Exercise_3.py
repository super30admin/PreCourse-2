# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes. On Geeksforgeeks
# Any problem you faced while coding this : No

import math
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next  
        
class LinkedList: 
  
    def __init__(self):
        # initializing head with none
        self.head = None
  
    def push(self, new_data): 
        # creating an object
        next_node = Node(new_data)
        if self.head:
            node = self.head
            while node.next:
                node = node.next
            node.next = next_node
        else:
            self.head = next_node

    # Function to get the middle of the linked list 
    def printMiddle(self): 
        length = 0
        if self.head:
            node = self.head
            while node.next:
                length += 1
                node = node.next
            # find the mid_index of the linked list
            mid_index = math.ceil(length / 2)
            node = self.head
            # interate over the found mid_index
            for _index in range(mid_index):
                node = node.next
            return node.data
        return None
        

# Driver code 
list1 = LinkedList() 

list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
print(list1.printMiddle())

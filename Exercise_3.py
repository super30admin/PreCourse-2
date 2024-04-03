# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode: I ran this code in VS Code editor in my local machine
# Any problem you faced while coding this: No

import math

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
        new_node = Node(new_data)

        if(self.head == None):
            self.head = new_node
        else:
            curr = self.head

            while curr.next != None:
                curr = curr.next

            curr.next = new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        cursor = self.head
        finder = self.head
        iterator = 1
        counter = 0

        while cursor != None:
            cursor = cursor.next
            counter += 1
        
        middle = math.ceil(counter/2)

        while iterator < middle:
            finder = finder.next
            iterator += 1
        print("Middle Data:", finder.data)
        
 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle()
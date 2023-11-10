# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach
# traversing the entire list to find the total number of nodes,
# divide list by total number of nodes to find middle 

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data):       #creating the list here
        newNode = Node(new_data)
        newNode.next = head
        head = newNode
        return head
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):      #traversing to find mid
        len = 0
        temp = self.head
        while (temp != None):
            len += 1
            temp = temp.next

        if head:
            mid = len // 2

        return mid


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

# Submitted by : Aryan Singh_RN12MAY2023
# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Not applicable
# Any problem you faced while coding this : No 
  
# Using the concept of slow and fast pointer. While fast pointer 
# jumps two nodes in each iteration, slow pointer jumps one node. 
# When fast pointer reaches the end, slow pointer moves one and at 
# end it will be at the middle of the linked list.

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
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
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

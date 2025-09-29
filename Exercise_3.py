
# Time Complexity : O(n) because we traverse the list once
# Space Complexity : O(1) because we only use two pointers
# Did this code successfully run on Leetcode : NA
# Any problem you faced while coding this : NA

# Node class for linked list
class Node:  
    # Initialize a node with data and next pointer
    def __init__(self, data):  
        self.data = data
        self.next = None
        
# Linked List class
class LinkedList: 
    def __init__(self): 
        self.top = None  # head of the list

    # Add a new element to the end of the list
    def push(self, new_data): 
        temp = Node(new_data)
        if self.top is None:  # if list is empty
            self.top = temp
        else:
            curr = self.top
            while curr.next:  # go to the last node
                curr = curr.next
            curr.next = temp  # attach new node at the end
        
    # Function to get the middle of the linked list
    def printMiddle(self): 
        slow = self.top  # moves one step at a time
        fast = self.top  # moves two steps at a time

        # traverse the list
        while fast is not None and fast.next is not None:
            fast = fast.next.next  # move fast pointer twice
            slow = slow.next       # move slow pointer once

        # when fast reaches end, slow is at the middle
       
        print( slow.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 

list1.printMiddle() 

# Node class
"""
// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None
// Your code here along with comments explaining your approach
Algorithm explanation
1) We use 2 pointer approach,where slow pointer moves 1 node ahead,whereas
fast pointer moves 2 nodes ahead
2) We get the middle node as the fast reaches the end of the list
"""

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

class LinkedList: 
  
    def __init__(self):
        self.head = None
  
    def push(self, new_data):
        newnode = Node(new_data)
        if not self.head:
            self.head = newnode
            self.head.next = None
        else:
            curr = self.head
            while curr and curr.next:
                curr = curr.next
            curr.next = newnode
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        curr = self.head
        slow = fast = curr
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
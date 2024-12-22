#  For getting middle element od the linked list:
# Time Complexity : O(n)
# Space Complexity : O(1)

#  Did this code successfully run on Leetcode : Yes, Leetcode 876 Middle of the Linked List

#  Any problem you faced while coding this : No

# Approach:
# I have used two pointers slow and fast. I have initialized both the pointers to the head of the linked list.
#  then slow pointer is incremented by 1 and fast pointer is incremented by 2.
#  When the fast pointer reaches the end of the linked list, the slow pointer will be at the middle of the linked list.
#  Finally, I have printed the data of the slow pointer.
 
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
        new_node.next = self.head
        self.head = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
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

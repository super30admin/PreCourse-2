# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : N/A, no Leetcode link
# Any problem you faced while coding this : Driver code and init code is not complete for python, 
# and  my driver code is not correct
# I have assumed that given a reference to head using slow-fast pointers can solve this problem

# Two pointers - fast and slow are set to head of list and until we don't see null values for fast pointer we loop
# Once fast pointer reach the end of list, slow pointer will be at middle of linked list

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.val = data
        self.next = None
    
class LinkedList: 
  
    def __init__(self): 
        self.head = Node()
        
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

# Time Complexity :O(N) 
# Space Complexity : O(1) 
# Did this code successfully run on Leetcode : I tried in VS code 
# Any problem you faced while coding this :No

# Node class  
# give you explanation for the approach
# In push just method adding a new node to the list
# In the print middle method I am using the slow/fast pointer approach to find the middle element
class Node:  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        new_head = Node(new_data)
        new_head.next = self.head
        self.head = new_head

    def printMiddle(self): 
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if slow:
            print("Middle element is:", slow.data)
        else:
            print("List is empty")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
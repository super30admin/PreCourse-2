# Time Complexity: O(n)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
'''
komalbhavake$ python3 Exercise_3.py
Middle Element is:  2
'''
# Your code here along with comments explaining your approach
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data
        self.next =None 
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
    def push(self, new_data): 
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head is None:
            return
        
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print(" Middle Element is: ", slow.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

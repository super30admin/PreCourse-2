'''
Time Complexity : O(n), where n is nodes in linked list
Space Complexity : O(1)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
Your code here along with comments explaining your approach:
Fast and slow pointer approach. Increment fast twice and slow once.
This will ensure when fast travelled till end, slow will reach till middle only
'''

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
        newnode = Node(new_data)
        if self.head == None:
            self.head = newnode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newnode
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print('Middle:'+ str(slow.data))


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

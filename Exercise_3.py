# Time Complexity :O(N)
# Space Complexity :O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
# Your code here along with comments explaining your approach: Traverse linked list using two pointers. Move one pointer by one and another pointer by two. When the fast pointer reaches the end slow pointer will reach middle of the linked list. 

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
  
    # Function to get the middle of the linked list 
    def printMiddle(self):
        slow = self.head
        fast = self.head
        if self.head is not None:
            while (fast is not None and fast.next is not None):
                fast = fast.next.next 
                slow = slow.next
            print("The middle element is: ", slow.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

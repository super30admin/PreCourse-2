# // Time Complexity : O(n)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

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
        # Insert node at the beginning
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 

        slow = self.head
        fast = self.head
        # Traverse till fast is not pointed to null
        while fast is not None and fast.next is not None:
            # Slow moves 1 step
            slow = slow.next
            # Slow moves 2nd step
            fast = fast.next.next
        # Since fast takes 2 steps at a time, and slow takes 1 step at a time - by the time fast reaches end, slow points to the middle node
        if slow:
            print(slow.data)
        else:
            print("Empty List")


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

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
        listnode = Node(new_data)
        # If head doesn't exist then it is the first node, so it is head node
        if not self.head:
            self.head = listnode
        # If head node exists, attach the node to the end of the linked list
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = listnode

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # Initialise slow and fast pointer to head
        slow = fast = self.head
        # Advance slow pointer by 1 step[ and fast pointer by 2 steps. When fast pointer reaches end, slow pointer reaches the middle.
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

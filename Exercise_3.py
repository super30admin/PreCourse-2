# // Time Complexity : O(n)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode :Yes
# // Any problem you faced while coding this :
# Yes the while loop condition was a lil tricky to recall


# // Your code here along with comments explaining your approach
# using fast and slow pointers in a while loop to get to the middle element.
# Initially both slow and fast pointers are assigned to head.
# slow ptr moves one stepo ahead and fast moves two steps ahead
# we terminate when fast reached the end of the linked list adn return position of slow ptr

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
        node = Node(new_data)
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        else:
            self.head = node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        
        fast = slow = self.head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        return slow

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

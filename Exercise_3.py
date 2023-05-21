# Time Complexity : O(1) for all operation
# Space Complexity : O(1) since only one extra variable needed
# Did this code successfully run on Leetcode : Did not find exact problem on Leetcode
# Any problem you faced while coding this : -

# The classic way is to use slow pointer, fast pointer to obtain the middle which takes O(n) time.
# However, since we did not the 'remove' function in this implementation. 
# I use a flipper variable "self.odd" to track every alternate insert into the linked list.
# For every alternate insert, I increment the "self.mid" pointer, 
# which can lead to O(1) lookups since `mid` only moves in one direction .

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.odd = False 
        self.head = None
        self.mid = None
  
    def push(self, new_data): 
        if not self.head:
            self.head = Node(new_data)
            self.mid = self.head
            self.odd = True
        else:
            self.head.next = Node(new_data)
            self.head = self.head.next
            self.odd = not self.odd
            if self.odd:
                self.mid = self.mid.next
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        return self.mid.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

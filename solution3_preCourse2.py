# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O(n)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : yes difficulty to understand which approach is better. Here I used two pointers one slow pointer
# & fast pointer two space at time.


class Node:
   
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
   
   
# Linked List class contains a Node object
class LinkedList:
   
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
 
    # Print the linked list
    def printList(self):
        node = self.head
        while node:
            print(str(node.data) + "->", end="")
            node = node.next
        print("NULL")
 
    # Function that returns middle.
    def printMiddle(self):
        # Initialize two pointers, one will go one step a time (slow), another two at a time (fast)
        slow = self.head
        fast = self.head
 
        # Iterate till fast's next is null (fast reaches end)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        # return the slow's data, which would be the middle element.
        print("The middle element is ", slow.data)
  
# Code execution starts here
if __name__=='__main__':
    
    # Start with the empty list
    llist = LinkedList()
    
    list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

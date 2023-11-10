# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :

# Your code here along with comments explaining your approach

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data): #Allocating the Node and putting in the data, making next of new Node as head
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node #Moving the head to point to new Node

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): #Traversing linked list using slow and fast pointers. Move one pointer by one and other pointer by two. When the fast pointer reaches end slow pointer will reach middle of the linked list.
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("The middle element is: ", slow_ptr.data)
            

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

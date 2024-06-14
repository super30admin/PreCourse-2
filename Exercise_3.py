#Time Complexity : O(n)
#Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Node class  
class Node:
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data  
        
class LinkedList:
    def __init__(self):
        self.head = None   
#Insert a new node with the given data at the beginning of the linked list 
    def push(self, new_data):
        new_data = Node(new_data) 
        new_data.next = self.head
        self.head = new_data 
        
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        first_ptr = self.head
        second_ptr = self.head
        #Returns middle element of the linkedlist
        while second_ptr and second_ptr.next:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next.next
        print("The Mid Element of Linked List is : ", first_ptr.data) 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

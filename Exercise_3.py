# Time Complexity : O(n): we traverse the list once using fast pointer which covers n steps in n/2 iterations
# Space Complexity : O(1): only two extra pointers (slow and fast) are used, no extra storage
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
#We build a linked list by inserting each new node at the front and use two pointers slow and fast both starting at head.
#In every iteration, slow moves 1 step and fast moves 2 steps, so when fast can't move forward anymore, slow has covered exactly half the list.
#At that point slow.data gives us the middle element directly without any second traversal.
# Your code here along with comments explaining your approach

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
       self.data = data   #where we are storing the entire data   
       self.next = None     #right now the pointer to the next element is set to none 
class LinkedList: 
  
    def __init__(self): 
        self.head = None    #no elements have been added so we start at none
        
        
  
    def push(self, new_data): 
        new_element = Node(new_data) # we are creating a new element 
        new_element.next = self.head        #we point the new element to the head element
        self.head = new_element         #now the new element is the head element 
        
        # adding in the front helps to keep the code simple
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head    #both slow and fast start at the head
        fast = self.head  
        
        #so by the time fast reaches the end, slow will reach the mid
        while fast is not None and fast.next is not None:
            slow = slow.next        #slow jumps by one spot
            fast = fast.next.next       #fast jumps by two spots
        print ("the Middle element is:",slow.data)
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
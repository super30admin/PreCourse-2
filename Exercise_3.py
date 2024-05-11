"""  
 
 Time Complexity : O(n)
 Space Complexity : O(1) 
 Did this code successfully run on Leetcode : Yes
 Any problem you faced while coding this : No


 Your code here along with comments explaining your approach :
 We're using slow and fast pointer approach i.e., slow moves to its next element in every iteration where as
 fast moves to its next next element so when the fast moves to end slow will be at the mid so that's the mid of SLL.
 """

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
            
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow_pointer, fast_pointer = None, None
        slow_pointer = fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next 
            fast_pointer = fast_pointer.next.next 
        
        if slow_pointer:
            print("Middle is ", slow_pointer.data)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

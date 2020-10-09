#Time Complexity : O(n/2)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : No, I did not run it on leetcode
#Any problem you faced while coding this : I am not sure on the complexity particularly space complexity


#Your code here along with comments explaining your approach

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
        # we add the node at the start of the linkedlist and make it self.head
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
        
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # here we take two pointers one slow and one fast
        # the slow pointer take 1 step the fast pointer takes two steps
        # when the fast pointer reaches end the element at slow pointer is cemter element of linked list
        slow_ptr = self.head
        fast_ptr = self.head 
        
        if self.head != None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                prev = slow_ptr
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
				
        if fast_ptr == None:
            print("The middle element is: {}, {} " .format(slow_ptr.data,prev.data) )
            return
            
        if fast_ptr.next == None:
            print("The middle element is: ", slow_ptr.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 


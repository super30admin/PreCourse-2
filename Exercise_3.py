# Time Complexity : O(n) for finding the middle (push is O(1))
# Space Complexity : O(n) to store n nodes in the list
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : No issues


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
        # start both pointers at the head
        slow = self.head
        fast = self.head

        # move fast by two and slow by one until fast hits the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # slow is now at the middle
        if slow:
            print("Middle element is", slow.data)
            



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle() 

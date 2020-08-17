# Node class  
# Using slow and fast pointers.
# Move the fast pointer by two steps and slow pointer by a single step.
# as soon as the fast pointer reaches the end of the linked list, slow pointer will still be in the middle (since it took single step).
# return the middle element.
# Time complexity - O(n)
# Space complexity - O(1)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
    	self.data = data
    	self.next = None
        
class LinkedList: 
  
    def __init__(self): 
    	self.head = None
        
  
    def push(self, new_data): 
    	# create a new node.
        newNode = Node(new_data)
        
        # push the new node to the end of the linked list.
        if not self.head:
        	self.head = newNode
        	return

        node = self.head

        # traverse the linked list.
        while node.next:
        	node = node.next
        node.next = newNode

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
    	slowptr = self.head
    	if not slowptr:
    		return None
    	fastptr = slowptr.next

    	while fastptr and fastptr.next:
    		slowptr = slowptr.next		# slow ptr moves to the next node
    		fastptr = fastptr.next.next	# fast ptr jumps one node to reach the end of the linked list while slow ptr reaches the middle.

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

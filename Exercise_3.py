# Approach - Set 2 pointers slow and fast
# every iteration move slow pointer by one position and fast by two
# when fast reaches end of LL or NULL pointer, the value slow pointer points at is the middle point
# Time Complexity -- O(N) as we pass through all the nodes and find mid point in a single pass
# Space Complexity -- O(1) Only 2 pointers used, not extra space required

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        
  
    def push(self, new_data):

        new_data = Node(new_data)
        if not self.head:
            self.head = new_data

        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_data

    # Function to get the middle of the linked list 
    
    def printMiddle(self): 
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head:
            while fast_ptr is not None and fast_ptr.next is not None:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            return slow_ptr.data


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
# list1.push(7)
val = list1.printMiddle()
print(val)

# Find Mid Point of a Singly Linked List.

# Time Complexity: O(n) (Since traversing the list only once.)
# Space Complexity: O(1)

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
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node 
         
    # Function to get the middle of the linked list
    # Fast and Slow pointer. For every 1 step of ptr1, ptr2 takes 2 steps.
    # So when ptr2 reaches end of LinkedList, ptr1 points to MidPoint.
    def printMiddle(self):
        ptr1 = self.head
        ptr2 = self.head
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = (ptr2.next).next
        
        print("Mid Point is ", ptr1.data)

# Driver code
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()
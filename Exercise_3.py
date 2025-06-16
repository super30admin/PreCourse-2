# Time Complexity: O(n) - Traverse the entire list once
# Space Complexity: O(1) - No extra space used, only two pointers

# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
# Linked List class
class LinkedList: 
    def __init__(self): 
        self.head = None
  
    # Function to insert a new node at the beginning
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Function to get the middle of the linked list 
    def printMiddle(self): 
        slow_ptr = self.head
        fast_ptr = self.head

        # Move fast pointer by 2 and slow pointer by 1
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        if slow_ptr:
            print("The middle element is:", slow_ptr.data)
        else:
            print("The list is empty.")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

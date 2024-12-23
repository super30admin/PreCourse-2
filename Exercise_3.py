# Node class
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Used slow and fast pointers to find the middle node
class Node:  
    # Function to initialize the node object  
    def __init__(self, data):  
        self.data = data  # Assign data to the node
        self.next = None  # Initialize next as None
class LinkedList: 
    def __init__(self):    
        self.head = None  # Initialize head of the linked list as None

    def push(self, new_data): 
        # Creating a new node and make it the head
        new_Node = Node(new_data)
        new_Node.next = self.head
        self.head = new_Node

    def printMiddle(self): 
        # Use slow and fast pointers to find the middle as fast is moving by 2 eventually when it reaches to end out slow will be at middle
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next  # slow by one step
            fast = fast.next.next  #  fast by two steps
        print(f"middle = {slow.data}")  # Slow is at middle node

# Driver code
list1 = LinkedList() 
list1.push(5)  # Add 5 to the list
list1.push(4)  # Add 4 to the list
list1.push(2)  # Add 2 to the list
list1.push(3)  # Add 3 to the list
list1.push(1)  # Add 1 to the list
list1.printMiddle()  # Print the middle element

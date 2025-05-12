# Time Complexity:
# - push(): O(1)
# - printMiddle(): O(n)
# Space Complexity: O(1)

# Any problem you faced while coding this: 
# Fast and slow pointers approach, couldn't come up with it myself, had to understand other solutions.


# Node class to represent each element in the list
class Node:  
    def __init__(self, data):  
        self.data = data
        self.next = None

# Linked List class
class LinkedList: 
    def __init__(self): 
        self.head = None

    # Insert a new node at the beginning
    def push(self, new_data): 
        new_node = Node(new_data)     # create a new node
        new_node.next = self.head     # point it to the old head
        self.head = new_node          # move head to new node

    # Function to print the middle element
    def printMiddle(self): 
        slow = self.head
        fast = self.head

        # Move fast by 2 and slow by 1 until fast reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # When fast reaches the end, slow is at the middle
        if slow:
            print("The middle element is:", slow.data)
        else:
            print("The list is empty.")

# Driver code to test
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()


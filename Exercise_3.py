#Time Complexity: Insertion (push) into the linked list is O(1) because it's a constant-time operation.
#Finding the middle of the linked list is O(n), where n is the number of nodes in the linked list.
# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning of the linked list
    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to find and print the middle of the linked list
    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while fast_ptr is not None and fast_ptr.next is not None:
                fast_ptr = fast_ptr.next.next  # Move two steps
                slow_ptr = slow_ptr.next  # Move one step

            print("The middle element is:", slow_ptr.data)

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

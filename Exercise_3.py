# Node class
class Node:
    # Time Complexity : O(1)
    # Space Complexity : O(1)
    # Any problem you faced while coding this : No
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Time Complexity : O(1)
    # Space Complexity : O(1)
    # Any problem you faced while coding this : No
    # Function to initialise the list
    def __init__(self):
        self.head = None

    # Time Complexity : O(1)
    # Space Complexity : O(1)
    # Any problem you faced while coding this : No
    # Function to create a new node and set it to the head
    def push(self, new_data):
        nodeToAdd = Node(new_data)
        nodeToAdd.next = self.head
        self.head = nodeToAdd

    # Time Complexity : O(n/2)
    # Space Complexity : O(1)
    # Any problem you faced while coding this : No
    # This function gets the middle of the list, two pointers are created. One iterates slowly, one node at a time. The other iterates faster, two nodes at a time.
    # When the fast node reaches the end, the slow node is at the middle and we can return the middle
    def printMiddle(self):
        slowPtr = fastPtr = self.head
        if self.head is not None:
            while fastPtr is not None and fastPtr.next is not None:
                slowPtr = slowPtr.next
                fastPtr = fastPtr.next.next
            print(slowPtr.data)

    # Time Complexity : O(n)
    # Space Complexity : O(1)
    # Any problem you faced while coding this : No
    # Helper function to print the list
    def printList(self):
        ptr = self.head
        while ptr.next:
            print(ptr.data)
            ptr = ptr.next
# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printList()
list1.printMiddle()

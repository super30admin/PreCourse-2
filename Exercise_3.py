# Node class
#Time Complexity : O(N)
#Space Complexity : O(1)
#Any problem you faced while coding this : No
#Traverse linked list with two pointers where we move one pointer by one and other pointer by two. When the  pointer 2 reaches end pointer 1  reaches the middle of the linked list.
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
        ptr1 = self.head
        ptr2 = self.head

        if self.head is not None:
            while (ptr2 is not None and ptr2.next is not None):
                ptr2 = ptr2.next.next
                ptr1 = ptr1.next
            print("The middle element is: ", ptr1.data)
# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

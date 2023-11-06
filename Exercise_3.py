# Node class
# Big-O Time & Space Complexity is O(n) since one needs to traverse through the nodes.

class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # data is representing the value of node object.
        self.next = None  # next is pointer to next node of node object.


class LinkedList:
    def __init__(self):
        self.head = None  # initializing empty linked list

    def push(self, new_data):
        new_node = Node(new_data)   # creates new_node with passed value
        new_node.next = self.head   # sets the new_node's next pointer to that of current head
        self.head = new_node        # sets existing head to that of the new_node node to append.

    # Function to get the middle of the linked list
    def printMiddle(self):
        if not self.head:
            return None

        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next        # Moves one step
            fast_pointer = fast_pointer.next.next   # Moves two steps
        return slow_pointer                         # When fast_pointer reaches end, slow_pointer would be half way thus that value is returned


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
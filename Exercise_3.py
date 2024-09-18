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
        new_node.next = self.head
        self.head = new_node

    # Function to get the middle of
    # the linked list

    # using tortoise and hair method, when fast pointer is at the last element, slow pointer is at the mid point
    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        print(slow_ptr.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

# time complexity is O(1) or push and O(n) for printing
# space complexity is O(1) for push and printing

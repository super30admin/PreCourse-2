# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self._DUMMY = Node(None)
        self._head = self._DUMMY
        self._tail = self._DUMMY

    def push(self, new_data):
        node = Node(new_data)
        self._tail.next = node
        self._tail = node

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        slow = self._head.next
        fast = self._head.next
        if fast is None:
            print(None)
            return

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

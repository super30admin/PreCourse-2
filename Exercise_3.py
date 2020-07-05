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
        node = Node(new_data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node


    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        if not self.head:
            print(None)
        else:
            slow_pointer = self.head
            fast_pointer = self.head
            while fast_pointer:
              if (fast_pointer.next):
                fast_pointer = fast_pointer.next
                slow_pointer = slow_pointer.next
              fast_pointer = fast_pointer.next
            print(slow_pointer.data)

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

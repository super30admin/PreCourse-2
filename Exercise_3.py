
"""

Time Complexity :O(Log(n))

"""

# Node class


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.end = None

    def push(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
            self.end = self.head

        else:
            newNode = Node(new_data)
            self.end.next = newNode
            self.end = self.end.next

        return False

    # Function to get the middle of
    # the linked list
    def printMiddle(self):

        fast = self.head.next
        slow = self.head
        if self.head is None:
            return
        while fast and fast.next:
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

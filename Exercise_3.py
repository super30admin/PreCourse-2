'''
Time Complexity - O(n)
Space Complexity - O(1)
'''


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        node = Node(new_data)
        node.next = self.head
        self.head = node

# using slow and fast pointer technique to find the middle of a linked list
    def printMiddle(self):
        slow = self.head
        fast = self.head

        if not self.head:
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(f"Middle of the linked list is: {slow.data}")

        # Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

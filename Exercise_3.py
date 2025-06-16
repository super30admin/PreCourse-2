# Time: O(N)
# Space: O(1)

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, new_data):
        new = Node(new_data)
        if not self.head:
            self.head = new
            self.tail = new
        else:
            node = self.tail
            node.next = new
            self.tail = new
        self.length += 1

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        ''' Slow and fast pointer approach'''
        slow = self.head
        fast = self.head
        while fast.next:
            slow = slow.next
            fast = fast.next.next
        print(f"middle data = {slow.data}")
        return slow.data

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

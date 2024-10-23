# Time complexity: Since there is a tail pointer, pushing to list is O(1)
# Finding the middle element takes O(n) as the pointer iterates through every element
# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.linkedList = self.tail = Node()

    def push(self, new_data):
        self.tail.next = Node(new_data)
        self.tail = self.tail.next

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        slow = fast = self.linkedList.next
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

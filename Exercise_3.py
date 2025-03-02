# Finding middle element of the LL using Tortoise hare method
# Time complexity: O(n) iterating through whole array with both pointers
# space complexity: O(1) only two pointer are getting used that can be neglacted so constant space
# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # insert new node/data at the beginning/ Head insertion
    def push(self, new_data):
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode

    # Function to get the middle of
    # the linked list
    # using tortoise-hare method
    def printMiddle(self):
        # both pointers starts from the head
        slow = self.head
        fast = self.head
        if self.head:
            while fast and fast.next:
                slow = slow.next  # slow moves one step
                fast = fast.next.next  # fast moves two steps
        print("The middle element is:", slow.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

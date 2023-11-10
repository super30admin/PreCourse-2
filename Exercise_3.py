# Time Complexity : O(N)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Couldn't find on Leetcode
# Any problem you faced while coding this : None
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
        node.next = self.head
        self.head = node

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        # implementing using two pointers 1 fast and 1 slow
        # fast travels at twice the speed of slow
        # when fast reaches end, slow reaches only to the middle
        slow = self.head
        fast = self.head

        if self.head is None:
            print("Empty list!")
        else:
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            print("The middle element is: %s" %str(slow.data))


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
# if number of elements are even print the n/2 element
list1.printMiddle()

# // Time Complexity : O(N)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode :
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach
"""
1. Use two pointers slow and fast , make slow traverse one element and fast by two elements at a time
2. When fast reaches end of the linked list , slow pointers reaches at middle of linkedlist
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

    def push(self, new_data):
        if not self.head:
            self.head = Node(new_data)
            return
        pos = self.head
        while pos.next:
            pos = pos.next
        pos.next = Node(new_data)

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle element is {}".format(slow.data))


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle() 

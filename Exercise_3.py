"""
Time Complexity : O(n)
Space Complexity : O(n)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
Your code here along with comments explaining your approach
"""
# Node class


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = Node(None)
        self.pointer = Node(None)
        self.pointer = self.head

    def push(self, new_data):
        if not self.head:
            self.head = Node(new_data)
        else:
            new = Node(new_data)
            self.pointer.next = new
            self.pointer = self.pointer.next

    # Function to get the middle of
    # the linked list

    def printMiddle(self):
        """
        I took a two pointer approach. A slow pointer and a fast pointer
        while the slow pointer is iterated once every loop, fast is iterated twice
        That is why, when fast reaches the end of the list, slow reaches the middle element
        """
        slow, fast = self.head, self.head
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

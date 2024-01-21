# Time Complexity : O(n) for all the below operations; n = length of list
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
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
        newNode = Node(new_data)
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = newNode

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        # fast moves 2x the speed of slow
        # when fast reaches end; slow should be in middle
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        print(slow.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

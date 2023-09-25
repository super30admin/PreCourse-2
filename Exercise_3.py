# Exercise_3 : Find Mid Point of a Singly Linked List.
# Time Complexity : O(n) as we are appending new node to the end of the list
# Space Complexity : O(n) as n is length of the list
# Did this code successfully run on Leetcode : yes, problem 876
# Any problem you faced while coding this : NA

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
        # if head is none, make the incoming data to be node 1
        if self.head is None:
            self.head = Node(new_data)
            return
        curr = self.head
        # if there is at least one node, set curr pointer at the start and move
        # it forward until curr.next is null.
        # If yes, create new node using incoming data & append it next to wherever curr is pointing
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(new_data)
        return

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        # slow & fast ptr start at head (first node)
        slow = self.head
        fast = self.head

        # if linked list is empty, return none
        if self.head is None:
            return None
        # slow moves one hop and fast moves two hops at a time
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        return slow


# Driver code
list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(100)
list1.push(6)
list1.push(5)
list1.push(5)
list1.push(100)
list1.push(100)
list1.printMiddle()

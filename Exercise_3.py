## Time Complexity : O(N2)
## Space Complexity : O(N)
## Did this code successfully run on Leetcode : Yes
## Any problem you faced while coding this : No
##
##
## Your code here along with comments explaining your approach
# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        if self.head is None:
            return None

        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next_node:
            slow_pointer = slow_pointer.next_node
            fast_pointer = fast_pointer.next_node.next_node

        return slow_pointer.data


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
print(list1.printMiddle())
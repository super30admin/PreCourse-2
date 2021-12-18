# Time Complexity:
#   * push: O(1)
#   * printmiddle: O(n)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        newnode = Node(new_data)
        newnode.next = self.head
        self.head = newnode

    # Function to get the middle of the linked list
    # using two pointers to get middle position in one pass
    # fast advances double the pace as slow
    def printmiddle(self):
        slow = self.head
        fast = self.head
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
list1.printmiddle()

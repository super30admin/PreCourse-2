# Node class

# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : No
# Approach - Use a fast and slow pointer. When the fast pointer reaches the end, slow pointer reaches the middle

class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            self.head.next = None
        else:
            new_node.next = self.head
            self.head = new_node

            # Function to get the middle of
            # the linked list

    def printMiddle(self):
        if not self.head:
            return None
        sp = self.head
        fp = self.head
        # move slow pointer by 1 and fast pointer by 2
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next

        return sp.data


        # Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
print(list1.printMiddle())

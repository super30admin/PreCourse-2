# time complexity: O(n)
# space complexity: O(1)
# Did this code successfully run on Leetcode : NA
# Any problem you faced while coding this : No
# give you explanation for the approach

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
        if self.head == None:
            self.head = Node(new_data)
        else:
            node = Node(new_data)
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        if self.head is None:
            return None
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer!= None and fast_pointer.next!= None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer.data


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
print(list1.printMiddle())

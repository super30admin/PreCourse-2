# Time Complexity : log(n)
# Space Complexity : O(n)

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # function to have default value for head
    def __init__(self):
        self.head = None

    # pushing new nodes at the end
    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    # Function to get the middle of
    # the linked list
    # Using slow and fast pointer, slow will jump one place and fast two places for each jump on slow
    # this way slow will point to the middle element by the time fast pointer reaches the end of the list
    def printMiddle(self):
        slow = fast = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            if fast.next is not None:
                fast = fast.next
        print(slow.next.data)

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

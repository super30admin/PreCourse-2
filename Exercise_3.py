"""
The approach for finding the mid point of linked list is considering the linked list as a circle
Consider two pointers, slow and fast, both initially at the head of the linked list.
Traverse the linked list until fast pointer reaches the end.
Move the slow pointer by one and fast pointer by two.
In this manner, slow pointer will reach the middle of the linked list.

Time Complexity: O(n)(As we are traversing the linked list)
Space Complexity: O(1)(As we are not using any extra space)

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
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to get the middle of
    # the linked list

    def printMiddle(self):
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print(f"The middle element is :{slow.data}")


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Initialize head of linked list.
    # Time complexity - O(1)
    # Space complexity - O(1)
    def __init__(self):
        self.head = None

    # Appending element to left of linked list. If no head,the new element is assigned as
    # head of linked list. If head exists then traverse linked list till the end and append
    # new element at the end.
    # Time complexity - O(n)
    # Space complexity - O(1)
    def push(self, new_data):
        if not self.head:
            self.head = Node(new_data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(new_data)
        return

    # Function to get the middle of the linked list. If no head return None. If only head exists
    # return head. Create 2 slow and fast pointer, moving 1 element and 2 elements at a time
    # respectively. When fast pointer reached end the slow pointer reached mid-point.
    # Time complexity - O(n)
    # Space complexity - O(1)
    def printMiddle(self):

        if not self.head:
            return self.head

        if not self.head.next:
            return self.head.data

        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
print(list1.printMiddle())

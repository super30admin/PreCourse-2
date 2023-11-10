# Time complexity:O(n)
# Space complexxity: O(1)

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
        if self.head == None:
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode

    # Function to get the middle of
    # the linked list

    def printMiddle(self):
        # use two pointer technique and advance the fast pointer two nodes at a time while slow pointer moves one node at a time. This way when fast pointer reaches the end of the list, slow pointer will point to the middle of the list.
        if self.head == None:
            raise Exception("LinkedList is empty!")
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

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

    def printList(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end="->")
            ptr = ptr.next
        print()

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        if not self.head:
            print("list is empty")
            return
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("middle element is %d" % slow.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printList()
list1.printMiddle()

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
        newNode.next = self.head
        self.head = newNode
        return self.head

    def printMiddle(self):
        slow = self.head
        fast = slow.next

        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        print(slow.data)


        # Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # initializing head here

    def push(self, new_data):
        newnode = Node(new_data)
        newnode.next = self.head
        self.head = newnode

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        # using the two pointer method
        first = self.head
        second = self.head
        # running while till the second pointer reached end
        while second and second.next:
            first = first.next
            second = second.next.next
        print(first.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()


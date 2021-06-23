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

    def printMiddle(self):

        first = self.head
        last = self.head

        if (self.head is not None):
            while (last is not None and last.next is not None):
                last = last.next.next
                first = first.next
            print("The middle element of the singly linked list is: ", first.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()


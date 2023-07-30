# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, new_data):
        new = Node(new_data)
        new.next = self.head
        self.head = new
        self.size = self.size + 1

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        temp1 = self.head
        temp2 = self.head
        while (temp1 and temp1.next and temp1.next.next):
            temp2 = temp1
            temp1 = temp1.next
        print(temp2.data)


# Driver code
list1 = LinkedList()
list1.push(8)
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

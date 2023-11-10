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
        current = self.head

        if current:
            # Loop until end of the list is reached
            while current.next:
                current = current.next
            # Append the new node as last element
            current.next = newNode
        else:
            # If head is none, append the new node as head
            self.head = newNode

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        current = self.head
        length = 0
        # Get the length of the linked list
        while current:
            current = current.next
            length = length + 1

		# Find the mid value from length
        mid = length // 2
        i = 0
        current = self.head
        while i < mid and current:
            i = i + 1
            current = current.next

        if current:
            return current.data

        return None

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
print(list1.printMiddle())

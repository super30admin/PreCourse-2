# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None  # head

    def push(self, new_data):
        """
        A function to insert new node at beginning 
        """
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        """
        return middle element in the linked list 
        """
        # When the fast pointer reaches the end 
        # slow pointer will reach the middle of the linked list.
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2) # middle 
list1.push(3)
list1.push(1)
print(list1.printMiddle())

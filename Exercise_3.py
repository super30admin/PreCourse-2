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
        if self.head is None:
            self.head = Node(new_data)
        else:
            new = Node(new_data)
            new.next = self.head
            self.head = new


    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        ptr_1 = self.head
        ptr_2 = self.head

        if self.head is not None:
            while (ptr_1 is not None and ptr_1.next is not None):
                ptr_1 = ptr_1.next.next
                ptr_2 = ptr_2.next
            print(ptr_2.data)



# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

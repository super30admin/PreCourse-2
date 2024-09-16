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
        '''
        Check if head is None, if yes
        Create Node as head. If head is
        Not None then iterate to end of
        Linked list and then append Node
        to it. Complexity O(n)
        '''
        if self.head is None:
            self.head = Node(new_data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = Node(new_data)

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        '''
        Create 2 pointers - Fast Pointer and
        Slow Pointer. Fast Pointer will move
        2 steps ahead of Slow Pointer. Once
        Fast Pointer reaches end of list then
        the point at which Slow Pointer stopped
        is the middle node.
        Time Complexity O(n/2)
        '''

        if self.head is None:
            print("No elements to print")
            return

        fastPtr = self.head
        slowPtr = self.head
        while fastPtr is not None and fastPtr.next is not None:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next

        print("The middle element is " + str(slowPtr.data))


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

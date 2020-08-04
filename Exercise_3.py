# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None
        self.curr=None

    def push(self, new_data):
        temp=Node(new_data)
        if self.head is None:
            self.head=temp
            self.curr=self.head
        else:
            self.curr.next=temp
            self.curr=self.curr.next

    # Function to get the middle of
    # the linked list
    def printMiddle(self):

        slowPointer=self.head
        fastPointer=self.head

        while fastPointer is not None and fastPointer.next is not None:

            slowPointer=slowPointer.next
            fastPointer=fastPointer.next.next

        print(slowPointer.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.push(9)
list1.printMiddle()

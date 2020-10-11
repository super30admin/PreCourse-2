# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def push(self, new_data):
        node= Node(new_data)
        if self.head is None:
            self.head = node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next = node



    # Function to get the middle of
    # the linked list
    def printMiddle(self): #use fast and slow pointers. slow pointer moves by one and fast pointer increments by two.
        fast=self.head
        slow=self.head
        while fast is not None and fast.next is not None: # when fast pointer reaches the end, it means slow pointer would have reached the middle.
            slow=slow.next
            fast = fast.next.next
        print(slow.data)



# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

#Time complexity: O(N)

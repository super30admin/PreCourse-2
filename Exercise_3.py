# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self,head=None):
        self.head = head

    def push(self, new_data):

        if self.head:
            current = self.head
            while (current.next):
                current = current.next
            current.next = Node(new_data)
            return
        else:
            self.head = Node(new_data)
        return

    def print(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


    # Function to get the middle of
    # the linked list
    def printMiddle(self):

        linked_list_len = 0
        current = self.head
        while(current):
            linked_list_len = linked_list_len+1
            current = current.next

        if linked_list_len == 0:
            return

        else:
            current = self.head
            for i in range(0, int(linked_list_len/2)):
                current = current.next
            print(current.data)



# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.push(3)
list1.push(1)
#list1.print()
list1.printMiddle()
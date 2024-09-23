# Node class  
class Node:

    # Function to initialise the node object
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.size = 0

    def push(self, new_data):
        curr = self.head
        while curr.next is not None:
            curr = curr.next

        new_node = Node(new_data)
        curr.next = new_node
        self.size += 1

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):

        if self.size <= 0:

            return -1

        mid = (self.size // 2) + 1
        curr = self.head
        for _ in range(mid):
            curr = curr.next

        return curr.value


# Driver code 
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
# list1.push(1)
# list1.push(0)
print(list1.printMiddle())
# list1.printMiddle()

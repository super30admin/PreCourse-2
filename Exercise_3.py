# Node class  
class Node:

    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, data):
        if not self.head:
            self.head = Node(data=data)
            self.count += 1
            return
        temp_head = self.head
        while temp_head.next is not None:
            temp_head = temp_head.next
        temp_head.next = Node(data=data)
        self.count += 1
        return

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        i = 0
        if self.count % 2 != 0:
            mid = (self.count // 2)
        else:
            mid = (self.count // 2) - 1
        temp_head = self.head
        while i < mid:
            temp_head = temp_head.next
            i += 1
        print(temp_head.data)


# Driver code 
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.push(0)
list1.push(-1)
list1.push(-2)
list1.printMiddle()

# Node class


# Time Complexity = O(n) Space Complexity = O(1)
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = Node(None)
        self.length = 0

    def push(self, new_data):
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node = Node(new_data)
        temp.next = new_node
        self.length += 1

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        mid = self.length // 2
        print("Mid index of LinkedList is ", mid)
        temp = self.head
        for i in range(mid + 1):
            temp = temp.next
        print("Mid of LinkedList is ", temp.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)

temp = list1.head
while temp:
    print(temp.data)
    temp = temp.next
print(list1.length)
list1.printMiddle()

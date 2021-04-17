# Node class  
class Node:

    # Function to initialise the node object
    def __init__(self, data, Next=None):
        self.data = data
        self.Next = Next


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        newNode = Node(new_data)
        if self.head is None:
            self.head = newNode
        else:
            tempPtr = self.head
            while tempPtr.Next is not None:
                tempPtr = tempPtr.Next
            tempPtr.Next = newNode

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        if self.head is None:
            return
        navigateptr = self.head
        traverseString = ''
        while navigateptr:
            print(navigateptr.data)
            traverseString += " " + str(navigateptr.data)
            navigateptr = navigateptr.Next
        return traverseString


insertdata = [34, 22, 11, 434, 90, 80, 67, 32]
list1 = LinkedList()
for element in insertdata:
    # print(element)
    list1.push(element)
print(list1.printMiddle())

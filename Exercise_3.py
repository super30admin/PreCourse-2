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
        if self.head == None:
            self.head = Node(new_data)
        else:
            tmp = Node(new_data)
            tmp.next = self.head
            self.head = tmp

    def getCount(self):
        tmp = self.head
        count = 0

        while (tmp):
            count += 1
            tmp = tmp.next
        return count

    # Function to get the middle of
    # the linked list

    def printMiddle(self):
        if self.head != None:
            length = self.getCount()
            tmp = self.head
            mid = length//2
            while mid != 0:
                tmp = tmp.next
                mid -= 1
            print(f"Middle element is {tmp.data}")

    def show(self):
        if self.head == None:
            print("Empty stack")
        else:
            tmp = self.head

            while(tmp != None):
                print(tmp.data)
                tmp = tmp.next
            return


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
list1.show()

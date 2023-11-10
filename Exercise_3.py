# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.len_list = 0

    # creating a new node
    def push(self, new_data):
        new_node = Node(new_data)

    # check if list is empty, if yes make head as the 1st node
        if self.head == None:
            self.head = new_node
        # if no, then point the last node to new node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        # increment the len of the list by 1 on every new element push
        self.len_list += 1

    # Function to get the middle of the linked list
    def printMiddle(self):
        mid_count = 0
        # if and else condition to function accordingly if the length of the list is odd or even
        if self.len_list % 2 == 0:
            mid_count = (self.len_list / 2) - 1
        else:
            mid_count = self.len_list // 2

        # starting from the head till the middle count of the list
        prev = self.head
        node = None

        for i in range(int(mid_count)):
            node = prev.next
            prev = node

        print(node.data)
        if self.len_list % 2 == 0:
            print(node.next.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
# list1.push(0)
# list1.push(8)
# list1.push(9)
list1.printMiddle()

# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head, self.count = None, 0

    def push(self, new_data):
        node = Node(new_data)
        if self.head is None:
            self.head = node
            self.count += 1
            return

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next

        self.count += 1
        cur_node.next = node

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        if self.count == 0:
            print(-1)
            return

        # iterate over the list till self.count // 2
        cur_node = self.head
        index = 0
        while cur_node.next:
            if index == (self.count // 2):
                # found the middle node
                print(cur_node.data)
                return
            cur_node = cur_node.next
            index += 1


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

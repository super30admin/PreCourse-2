# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("The middle element is: ", slow_ptr.data)

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
# Driver code
if __name__ == '__main__':
    list1 = LinkedList()
    list1.push(5)
    list1.push(4)
    list1.push(2)
    list1.push(3)
    list1.push(1)
    list1.printList()
    list1.printMiddle()
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
        if self.head is None:
            self.head = Node(new_data)
        else:
            current_pointer = self.head
            while current_pointer.next is not None:
                current_pointer = current_pointer.next
            current_pointer.next = Node(new_data)

    # Function to get the middle of  
    # the linked list 
    def print_middle(self):
        total_length = 0
        current_pointer = self.head
        while current_pointer is not None:
            total_length += 1
            current_pointer = current_pointer.next
        middle_point = int(total_length / 2)
        total_length = 0
        current_pointer = self.head
        while current_pointer is not None:
            if total_length == middle_point:
                print(current_pointer.data)
            total_length += 1
            current_pointer = current_pointer.next


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.print_middle()

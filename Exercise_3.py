# Node class  
class Node:

    # Function to initialise the node object  
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.curr_ptr = None

    def push(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            self.curr_ptr = self.head
        else:
            new_node = Node(new_data)
            self.curr_ptr.next = new_node
            self.curr_ptr = new_node


    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if not self.head.next:
            return self.head

        ptr1 = self.head
        ptr2 = self.head

        while ptr2.next and ptr2.next.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next

        print("The middle element of the list is", ptr1.val)

# Driver code 


list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

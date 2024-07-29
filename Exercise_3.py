# Node class
class Node:
    def __init__(self, data):
        """
        Initialize a node with the given data and next pointer as None.
        
        :param data: The value to be stored in the node.
        """
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def push(self, new_data):
        """
        Insert a new node with the given data at the beginning of the list.
        
        :param new_data: The data to be inserted into the new node.
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printMiddle(self):
        """
        Print the middle element of the linked list.
        Uses the two-pointer technique to find the middle element.
        """
        slow = self.head
        fast = self.head
        
        if self.head is None:
            print("The list is empty.")
            return
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print(f"The middle element is: {slow.data}")

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

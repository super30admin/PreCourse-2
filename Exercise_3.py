# Time: O(n); Space: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """Insert at the head in constant time."""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printMiddle(self):
        """Print the middle value; for even lengths, choose the second middle."""
        slow = self.head
        fast = self.head
        if slow is None:
            print("The list is empty.")
            return

        # Fast advances twice as quickly, so slow is at the midpoint at the end.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print("The middle element is", slow.data)


if __name__ == "__main__":
    list1 = LinkedList()
    for value in [5, 4, 2, 3, 1]:
        list1.push(value)
    list1.printMiddle()

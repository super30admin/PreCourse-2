"""
Time Complexity : O(n*log(n) )
Space Complexity : O(n)
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def findmiddle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return print(slow.data)


if __name__ == "__main__":
    link_list = LinkedList()
    for i in range(7, 0, -1):
        link_list.push(i)
    link_list.findmiddle()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_middle(self):
        if self.head is None:
            return
        else:
            slow=self.head
            fast=self.head
            while(fast and fast.next):
                fast=fast.next.next
                slow=slow.next
        return slow.data

list = LinkedList()
list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)
print(list.print_middle())

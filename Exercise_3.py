# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data=0):
        self.val = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.root = None

    def push(self, new_data):
        if not self.root:
            self.root = Node(new_data)
        else:
            cur = self.root
            while cur.next:
                cur = cur.next
            cur.next = Node(new_data)


    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        if not self.root:
            print("No Elements")
        else:
            slow,fast = self.root, self.root

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            print("Middle Element :",slow.val,"\n")

    def display(self):
        cur = self.root
        while cur:
            print(cur.val,end = ' ')
            cur = cur.next

    
# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push( 2)
list1.push(3)
list1.push(1)
# list1.display()
list1.printMiddle()

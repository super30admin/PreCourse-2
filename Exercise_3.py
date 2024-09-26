# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None
    def push(self, new_data):
        newNode=Node(new_data)
        if self.head==None:
            self.head=newNode
            return
        traverseNode=self.head
        while traverseNode.next!=None:
            traverseNode=traverseNode.next;
        traverseNode.next=newNode
    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        front=self.head
        back=self.head
        while front!=None and front.next!=None:
            front = front.next.next
            back=back.next
        print(back.data)

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)

list1.printMiddle()

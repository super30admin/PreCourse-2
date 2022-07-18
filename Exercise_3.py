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
        if self.head==None:
            self.head=Node(new_data)
        else:
            node=self.head
            while node.next:
                node=node.next
            node.next=Node(new_data)



    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        c=1
        l=self.head
        while l.next!=None:
            l=l.next
            c+=1
        l=self.head
        for i in range(c//2):
            l=l.next
        print(l.data)

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

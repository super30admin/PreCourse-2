# 3. Python program for implementation for finding Mid Point of a Singly Linked List

# tc - o(n/2) 
# sc - o(1)

class Node:

    # Function to initialise the node object
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self,newdata):
        self.data=newdata

    def set_next(self,newnext):
        self.next=newnext

class LinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    #the linkedlist will be like this-- head -> 5-> 4-> 2-> 3-> 1 ->none
    def push(self, new_data):
            temp=Node(new_data)
            temp.set_next(self.head)
            self.head=temp
            self.size=self.size+1

    # Function to get the middle of the linked list
    def printMiddle(self):
        current=self.head
        middle=self.size//2
        size=0
        while (size !=middle) &(size<=middle):
            current=current.get_next()
            size=size+1
        return current.get_data()

# Driver code
list1 = LinkedList()
list1.push(5)
print(list1.printMiddle())
list1.push(4)
print(list1.printMiddle())
list1.push(3)
print(list1.printMiddle())
list1.push(2)
print(list1.printMiddle())
list1.push(1)
print(list1.printMiddle())
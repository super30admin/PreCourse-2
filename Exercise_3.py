# Time Complexity : O(N)
# Space Complexity : O(1)

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None

    def getLength(self):
        if self.head == None:
            return 0

        else:
            count = 0
            moverNode = self.head
            while (moverNode):
                moverNode = moverNode.next
                count = count+1
        return count

    def push(self, new_data):

        if self.head == None:
            self.head = Node(new_data)

        else:
            tempNode = Node(new_data)
            tempNode.next = self.head
            self.head = tempNode

    def show(self):

        moverNode = self.head
        while (moverNode):
            print(moverNode.data)
            moverNode = moverNode.next

    # Function to get the middle of
    # the linked list
    def printMiddle(self):

        if self.getLength() == 0:
            return "List is Empty"
        else:
            if self.getLength() % 2 == 0:
                move = (self.getLength()//2)-1
                move1 = (self.getLength()//2)
                moverNode2 = self.head
            else:
                move = (self.getLength()//2)
            moverNode = self.head
            count = 0
            while (count < move):
                moverNode = moverNode.next
                count = count+1
            count = 0
            if self.getLength() % 2 == 0:
                while (count < move1):
                    moverNode2 = moverNode2.next
                    count = count+1

                print("Middle Element :", moverNode2.data)

            print("Middle Element :", moverNode.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.show()
list1.printMiddle()

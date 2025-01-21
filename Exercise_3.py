# Node class  
class Node:

    # Function to initialise the node object  
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    # def printLL(self):
    #     tempNode = self.head
    #     while (tempNode):
    #         print(tempNode.data)
    #         tempNode = tempNode.next

    def getLen(self):
        count = 0
        tempNode = self.head

        while tempNode is not None:
            count += 1
            tempNode = tempNode.next
        return count

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head is not None:
            # get length of the LL
            length = self.getLen()

            # temp reference to head
            curr = self.head
            # mid of length
            mid_val = length // 2

            # while traversing through list
            # as long as mid != 0, traverse further
            # decrement value of mid after every node
            # once mid is equal to 0, mid-value is achieved
            # return curr node value
            while mid_val != 0:
                curr = curr.next
                mid_val -= 1
            print("Middle value is: ", curr.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
# list1.printLL()
print("length: ", list1.getLen())
list1.printMiddle()

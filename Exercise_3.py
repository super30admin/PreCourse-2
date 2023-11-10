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
        """
        Time complexity - O(1)
        Space complexity - O(1)
        """
        new_node = Node(new_data)

        # if head is not empty
        # assign new nodes next to old head
        new_node.next = self.head
        # assign head to new_node
        self.head = new_node
        return self.head

    # print LL
    def printll(self):
        tempNode = self.head
        while (tempNode):
            print(tempNode.data)
            tempNode = tempNode.next

    # Get length of LL to find mid value
    def getLen(self, head):
        # count variable to count length of LL
        count = 0
        # create temp head reference
        temp = self.head

        while temp is not None:
            # increment count while traversing through the LL
            count += 1
            temp = temp.next
        return count

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        """
        Time complexity -O(n)
        Space complexity - O(1)
        """
        if self.head is not None:
            # get length of the LL
            length = self.getLen(self.head)

            # temp reference to head
            curr = self.head
            # mid of length
            mid_val = length // 2

            # while traversing through list
            # as long as mid != 0, traverse further
            # decrement value of mid after every node
            # once mid is equal to 0, mid value is achieved
            # return curr node value
            while mid_val != 0:
                curr = curr.next
                mid_val -= 1
            print(curr.data)


# Driver code 
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printll()
print("Middle node: ")
list1.printMiddle()

# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        # creating a linked list
        self.head = None

    def push(self, new_data):
        # Create a node for the data to insert
        nextNode = Node(new_data)
        nextNode.next = self.head
        self.head = nextNode
        # checking if linked list is empty or not and making new node ie., nextNode as head
        # if self.head is None:
        #     self.head = nextNode
        # #if not traverse till end
        # lastNode = self.head
        # while (lastNode.next):
        #     lastNode = lastNode.next
        # #updating the nextNode of lastNode
        # lastNode.next = nextNode

    # Function to get the middle of the linked list
    def printMiddle(self):
        count = 0
        middleNode = self.head
        while(self.head != None):
            # checking if count if odd, then update the middle node value
            if (count % 2 != 0):
                middleNode = middleNode.next
            count += 1
            self.head = self.head.next

        # if the given list is empty
        if(middleNode != None):
            print(middleNode.data)

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.push(7)
list1.push(10)
list1.printMiddle()

# Time Complexity : O(n/2) ~ O(n)
# Space Complexity :  I believe this should be O(1). Because I'm just storing constant items. Kindly confirm
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Not a challenge as such. I also thought of an alternate approach of using Recursion to do the same thing.
# For my approach, if there are even items in the linked list, I'm assuming the lower index to be the middle element
from hashlib import new


class Node:

    # Function to initialise the node object
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        # Head is the first element of the Linked List
        self.head = None

    def push(self, new_data):
        """
        Function to append nodes at the end of the Linked List

        :return: None
        """
        node = Node(new_data)

        if self.head is None:
            self.head = node
        else:
            # Temporary Object to hold the newly created Node
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def printlist(self):
        """
        Function to Print the Elements of the Linked List

        :return: None
        """
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp is not None:
                print("{} - >".format(temp.data))
                temp = temp.next
            print("\n")

    def printMiddle(self):

        if self.head is None:
            print("Linked List is Empty. No Middle Element")
            return "Middle Not Found"

        elif self.head.next is None:
            print("Only one element in Linked List. Middle couldn't be determined")
            return "Middle Not Found"

        node_1 = self.head
        node_2 = self.head.next
        while node_2 is not None and node_2.next is not None:
            node_1 = node_1.next
            node_2 = node_2.next.next

        print("Middle Element is {}".format(node_1.data))
        return "Middle Found"


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printlist()
list1.printMiddle()

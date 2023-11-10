""""// Time Complexity : 44ms
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach"""

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data=data
        self.next=None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next=self.head
        self.head=new_node

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        # Initialize two pointers, one will go one step a time (slow), another two at a time (fast)
        p1 = self.head
        p2 = self.head

        # Iterate till fast's next is null (fast reaches end)
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        # return the slow's data, which would be the middle element.
        print("The middle element is ", p1.data)



# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
# Exercise_3 : Find Mid Point of a Singly Linked List.
# // Time Complexity : push --> O(n), printMiddle --> O(n)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach

# Node class
class Node:  

    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, new_data):
        new_node = Node(new_data)
        # check if LL is empty
        if self.size == 0:
            # if empty then set the new_node as head
            self.head = new_node
        # Otherwise
        else:
            # make current with the head
            current = self.head
            # check if next element in current
            while current.next:
                # updating current till the last element is found
                current = current.next
            # appending new node
            current.next = new_node
        self.size += 1

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        #slow and fast  ptr set to head
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # when fast reached end, slow reaches middle
        return slow.data

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

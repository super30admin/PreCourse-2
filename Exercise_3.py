'''
# Exercise_3 : Python program to find Mid Point of a Singly Linked List.

# Description: Find Mid Point of a Singly Linked List.

# Author: Neha Doiphode
# Date  : 06-17-2022

# Approach:
    * Approach 1: Find length of the linked list.
                  Once we know the length, traverse to the mid point of the list and return the mid point.

    * Approach 2: Use fast and slow pointers.
                  Create fast pointer such that it traverses twice as fast as the slow pointer.
                  When fast pointer reaches end of the list, slow pointer must be pointing to the middle.


# Time Complexity                            : For both approaches,
                                               O(n), both approaches require traversing the list once.

# Space Complexity                           : For both approaches,
                                               O(1), no auxiliary space is used.

# Did this code successfully run on Leetcode : Yes(Problem 876).
# Any problem you faced while coding this    : Nothing critical.
'''

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def find_length(self, head):
        current = head
        length = 0
        while current:
            current = current.next
            length += 1
        return length

    def push(self, new_data):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(new_data)
        else:
            self.head = Node(new_data)

    # Function to get the middle of
    # the linked list
    def display(self, node):
        while node.next:
            print(f'{node.data} -> ', end = '')
            node = node.next
        print(f'{node.data}', end = '')
        print()
        print()

    def printMiddle(self):
        length = self.find_length(self.head)
        middle = length // 2
        current = self.head
        while middle:
            middle -= 1
            current = current.next
        self.display(current)

    '''
    Not part of the boilerplate. Added by Neha.
    '''
    def printMiddle_approach2(self):
        fast_ptr = slow_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        self.display(slow_ptr)

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
print('Approach 1: Find middle node of the linked list by finding length of linked list: ')
list1.printMiddle()
print('Approach 2: Find middle node of the linked list with fast and slow pointers: ')
list1.printMiddle_approach2()

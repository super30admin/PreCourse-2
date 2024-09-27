"""
Problem - Find the middle node of a singly linked list
Example - Input: [1,2,3,4,5]
          Output: 3
Solution -  Use two pointers - slow and fast. When traversing the list with a pointer slow,
            make another pointer fast that traverses twice as fast.
            When fast reaches the end of the list, slow must be in the middle.
Time Complexity - O(n), where n is the number of nodes in a given list
Space Complexity - O(1), the space used by slow and fast pointers
Test Cases - Edge Cases - Empty list, duplicates
             Base Cases - List with 1 node, sorted list
             Regular Cases - unsorted list with many elements
"""


# Node class
class ListNode:
    # Function to initialise the node object  
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
  
    def push_new_node(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Function to get the middle of the linked list
    def print_middle_node(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("The middle node of a Linked List is: ", slow.data)


# Driver code 
list1 = LinkedList()
list1.push_new_node(5)
list1.push_new_node(4)
list1.push_new_node(2)
list1.push_new_node(3)
list1.push_new_node(1)
list1.print_middle_node()

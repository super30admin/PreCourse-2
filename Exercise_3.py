# Python program to print middle node of singly linkedlist
# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : None
# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self): # creating empty linkedlist
        self.head = None

    # pushing data into the linkedlist
    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None: # checking if node is Empty and initialising it to new node
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        node = self.head
        if node is None:
            print("Linked list is empty")
        else:
            arr = []
            print("The Final LinkedList is")
            while node is not None:
                print(node.data,"----->",end = " ")
                arr.append(node.data)
                node = node.next
            mid = len(arr) // 2
            print(f"\nThe mid point of the linkedlist is {arr[mid]}")

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(6)
list1.push(8)
list1.push(1)
list1.push(2)
list1.printMiddle()

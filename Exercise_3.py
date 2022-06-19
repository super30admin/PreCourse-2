# Node class
"""
TC: O(n)
SC: O(1)

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printMiddle(self):
        ptr1 = self.head
        ptr2 = self.head
        # ptr1 will catch upto ptr2, while ptr2 checks for the last element.
        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        print("The middle element is ", ptr1.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

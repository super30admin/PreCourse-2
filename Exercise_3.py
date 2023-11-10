# Time Complexity: O(n)
# Space Complexity: O(1) extra space

# Node class
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next= None

class LinkedList: 
  
    def __init__(self):
        self.head = None
  
    def push(self, new_data): 
        if self.head is None:
            self.head = Node(new_data)
            return

        c = self.head

        while c.next is not None:
            c = c.next

        c.next = Node(new_data)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):

        if self.head is None:
            print(None)
            return

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle() 

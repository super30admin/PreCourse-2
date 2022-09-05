# Time Complexity: O(n)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Node class
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, new_data):
        new_node = Node(new_data)
        self.length = 0
        if self.head:
            node = self.head
            self.length += 1
            while node.next is not None:
                node = node.next
                self.length += 1
            node.next = new_node
            self.length += 1
        else:
            self.head = new_node
            self.length = 1

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.length %2 == 0:
            mid_length = self.length/2
        else:
            mid_length = self.length//2 + 1
        print(f'length: {mid_length}')
        current_length = 0
        if self.head:
            node = self.head
            while current_length < mid_length:
                node = node.next
                current_length += 1
            if node:
                print(node.data)


# Driver code 
list1 = LinkedList() 
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1) 
list1.printMiddle() 

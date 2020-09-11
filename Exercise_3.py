import math
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
class LinkedList: 
  
    def __init__(self): 
        self.node = None
  
    def push(self, new_data): 
        new_node = Node(new_data)
        if self.node == None:
            self.node = new_node
        else:
            head = self.node

            while head.next:
                head = head.next
            head.next = new_node
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 

        # Approach 1: Time Complexity: O(N)
        # Iterate till the end of the linked list. Find out how many elements are there and find the mid point.
        # Start iterating again till the mid point and print the value
        # pointer = self.node
        # i = -1
        # while pointer:
        #     pointer = pointer.next
        #     i += 1

        # pointer = self.node
        # mid = math.ceil(i / 2)
        # j = 0
        # while j <= mid:
        #     pointer = pointer.next
        #     j += 1
        
        # print(pointer.data)
        # return pointer

        # Approach 1: Time Complexity: O(N)
        # Fast and slow pointer approach where you iterate one pointer twice as fast as the other. By the end the slow pointer is pointing
        # to the middle node.
        slow, fast = self.node, self.node
        
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
        print(slow.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

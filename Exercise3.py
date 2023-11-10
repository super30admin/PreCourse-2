# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : N/A
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


    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head 
        fast = self.head
        if self.head is not None:
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next
        print(slow.data)

# Driver code 
list1 = LinkedList() 
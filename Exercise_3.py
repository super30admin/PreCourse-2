# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Some implementation issues

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = None

    # Adds new node to Linked list from the beginning
    def push(self, new_data): 
        item = Node(new_data)
        item.next = self.head
        self.head = item
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        length = 0
        cur_node = self.head

        #Traverses the linked list to get its length
        while cur_node:
            length += 1
            cur_node = cur_node.next
        
        mid = length // 2

        #Traverses the linked list again till the middle
        cur_node = self.head
        for i in range(mid):
            cur_node = cur_node.next
        #prints the middle of the linked list
        print(cur_node.data)
            
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()

# Time complexity: O(n)

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next  
        
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
        if self.head != None:
            curr = self.head
            list_length = 0
            while (curr != None):
                list_length += 1
                curr = curr.next
            curr = self.head
            middle_index = list_length // 2
            while middle_index > 0:
                curr = curr.next
                middle_index -= 1
            print(curr.data) 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

# Node class  
from tkinter.messagebox import NO


class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
  
    def push(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
        else:
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = Node(new_data)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow_node = self.head
        fast_node = self.head
        # print(slow_node.data, fast_node.data)
        while fast_node != None and fast_node.next != None :
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        
        print(slow_node.data)
        return slow_node.data

# Driver code de.next
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()

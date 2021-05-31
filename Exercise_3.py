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
        node_new = Node(new_data)
        node_new.next = self.head
        self.head = node_new

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # Take 2 pointers
        # pointer 1 moves by one
        # pointer 2 moves by 2
        ptr1 = self.head
        ptr2 = self.head
        if self.head is not None:
            while(ptr2 is not None and ptr2.next is not None):
                ptr2 = ptr2.next.next
                ptr1 = ptr1.next
            print("The middle element is ", ptr1.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle() 

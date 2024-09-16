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
        if self.head is None:
            self.head = Node(new_data)

        else:
            current_pointer = self.head
            self.head = Node(new_data)
            self.head.next = current_pointer

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):

        current = self.head
        mid_pointer = self.head
        while mid_pointer is not None:
            if mid_pointer.next is None:
                break
            else:
                current =current.next
                mid_pointer = mid_pointer.next.next
        print(current.data)
# Driver code
list1 = LinkedList()
list1.push(5) 
list1.push(4)
list1.push(9)
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

# Node class
# Time Complexity : o(n)
# Space Complexity : O(1)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.next = None
        self.data = data
        
class LinkedList: 
    # initialize the node
    def __init__(self):
        self.head = None
        
  
    def push(self, new_data):
        # Create new node and shift the head accordingly
        current_node = Node(new_data)
        current_node.next = self.head
        self.head = current_node
        # Function to get the middle of
    # the linked list 
    def printMiddle(self):
        big_pointer = self.head
        small_pointer = self.head

        # Keep two pointer with below specification:
        # big_pointer will move by two place
        # small_pointer will move by one place
        # so when big_pointer is at the end of the linked list then small array will be at the mid of the linked list
        while big_pointer != None:
            if big_pointer.next != None:
                big_pointer = big_pointer.next.next
            else:
                print (small_pointer.data)
                break
            if small_pointer.next != None:
                small_pointer = small_pointer.next


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

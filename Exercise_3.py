# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.value = data
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
        if not self.head:
            return None

        first_pointer = self.head
        second_pointer = self.head

        while second_pointer is not None and second_pointer.next is not None:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next.next

        return first_pointer.value

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
middle_pointer = list1.printMiddle() 
print("The middle element is", middle_pointer)

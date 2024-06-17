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
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(new_data)
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow_p = self.head
        fast_p = self.head

        if slow_p is None:
            return None

        else:
            while fast_p and fast_p.next:
                slow_p = slow_p.next
                fast_p = fast_p.next.next


        return print(slow_p.data)


# Driver code 
list1 = LinkedList() 
# list1.push(6)
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
# middle_node = list1.printMiddle()
# if middle_node is not None:
#     print("The middle element is: %d " % middle_node.data)
# else:
#     print("The list is empty.")

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None

class LinkedList: 
  
    def __init__(self): 
        self.head=None
  
    def push(self, new_data): 
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        fast_pointer=self.head
        slow_pointer=self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer=slow_pointer.next
            fast_pointer=fast_pointer.next.next
        
        print(f"The mid of this linkedlist is:{slow_pointer.data}")


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

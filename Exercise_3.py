# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data = 0):
        self.next = None
        self.data = data
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
    def push(self, new_data): 
        if self.head is None:
            self.head = Node(new_data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(new_data)

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head is None:
            print("LinkedList is very  empty")
        else:
            slow = fast = self.head
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next
            print(slow.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(4)
list1.printMiddle() 

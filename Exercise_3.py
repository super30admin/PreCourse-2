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
        newNode = Node(new_data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = newNode

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow_pointer = self.head
        fast_pointer = self.head
        if self.head.next is None or self.head.next.next is None:
            print(self.head.data, "Middle element")
        while(fast_pointer.next!=None and fast_pointer.next.next!=None):
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        print("Middle element", slow_pointer.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(0) 
list1.printMiddle() 
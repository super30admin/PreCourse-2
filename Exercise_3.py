# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.tail = None
        
  
    def push(self, new_data): 
        if self.tail == None:
            self.tail = Node(new_data)
            self.head = self.tail
        
        else:
            self.tail.next = Node(new_data)
            self.tail = self.tail.next
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow, fast = self.head, self.head
        while fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle of the Linked List is ", slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

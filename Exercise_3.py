# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data,next):  
        self.data = data
        self.next = next

class LinkedList: 
  
    def __init__(self): 
       self.head = None 
  
    def push(self, new_data): 
       node = Node(new_data,self.head)
       self.head = node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if not self.head or not self.head.next:
            return self.head 
        fast = self.head.next
        slow = self.head
        while fast:
            fast = fast.next
            if not fast:
                break
            fast = fast.next 
            slow = slow.next

        print(slow.data)
# Driver code 
list1 = LinkedList() 
list1.push(2) 
list1.push(5) 
list1.push(6) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

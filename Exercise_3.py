# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.val = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.tail = None
  
    def push(self, new_data): 
        if not self.head:
            self.head = Node(new_data)
            self.tail = self.head
        else:
            self.tail.next = Node(new_data)
            self.tail = self.tail.next
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # tc O(n), sc O(1).
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

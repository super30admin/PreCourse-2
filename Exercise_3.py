# Space Complexity - O(n) (Linked list to store n values)
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    # Time Complexity - O(1)
    def push(self, new_data): 
        if self.head is None:
            self.head = Node(new_data)
        else:
            newNode = Node(new_data)
            newNode.next = self.head
            self.head = newNode
  
    #Time Complexity - O(n)
    def printMiddle(self): 
        if self.head == None:
            print('Linked list is empty')
            return 
        slow = self.head
        fast = slow
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print slow.data
        
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

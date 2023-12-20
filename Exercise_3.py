# Node class  
#TC = O(n)
#SC = O(1)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, value):  
        self.value = value
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_value): 
        newNode = Node(new_value)
        newNode.next = self.head
        self.head = newNode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow, fast = self.head, self.head
        if self.head is not None:
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            print("Middle Element:", slow.value)
        else:
            print("Empty List")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

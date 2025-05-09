#TC => O(n) (Note: program will print the left middle element out of two if even length of linkedlist)
#s.c => O(n)
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = Node(-1)
        self.headRef = self.head
  
    def push(self, new_data): 
        self.head.next = Node(new_data)
        self.head = self.head.next

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        head = self.headRef
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

# Node class 

# keep adding the elements to the list when we perform a push operation
# inorder to get the middle of the list we use slow and fast pointers
# the slow pointer goes one by one but the fast pointer goes through two nodes at a time.
# when the fast pointer is at the end of the list the slow is at the middle

 
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None, next=None):  
        self.data = data
        self.next = next
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
    def push(self, new_data): 
        new_node = Node(new_data)    
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head:
            slow, fast = self.head, self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            print(slow.data)
        else:
            print("List is  empty")
        
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

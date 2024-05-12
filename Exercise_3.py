# Time complexity:  O(n)

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
        node = Node(new_data) 
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node    
  
    # Function to get the middle of  
    # the linked list 
    # Use tortoise and hare algorithm. Consider fast pointer is twice as fast as slow pointer.
    # when fast pointer reaches at the end, slow pointer reaches at the middle.
    # when elements are odd, fast pointer will be last node and when elements are even, fast pointer will be NULL to be 
    def printMiddle(self): 
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle()) 

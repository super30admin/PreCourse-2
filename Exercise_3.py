# TC : O(N)
# SC : O(1)
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
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
         
    def printMiddle(self):
        # Function to get the middle of  
        # the linked list
        slow_ptr = fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        print("Middle element is:",slow_ptr.data)

# Driver code 
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.push(0)
list1.printMiddle()
# Time Complexity: O(n)
# Space Complexity: O(n)

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None                # Initialize the head pointer.
  
    def push(self, new_data): 
        node = Node(new_data)
        if self.head == None:           # If head is empty.
            self.head = node
            return
        if self.head.next == None:      # If head is the only element.
            self.head.next = node
            return
        curr = self.head
        while curr.next != None:        # Traversing the list
            curr = curr.next
        curr.next = node
        return
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = fast = self.head                         # Initialize slow and fast pointers.
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print("Middle Element: " + str(slow.data))


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

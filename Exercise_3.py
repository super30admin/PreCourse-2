# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.value = data
        self.next = None  

        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data):
        
        new_node = Node(new_data) 
        
        curr = self.head
        
        if curr is None:
            self.head = new_node
            return
        
        while curr.next is not None:
            curr = curr.next
            
        curr.next = new_node 
        
    def printList(self):
        node = self.head
        
        while node is not None:
            print(f"{node.value}") 
            node = node.next  
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # solving using fast and slow pointers
        
        slow = self.head
        fast = self.head 
        
        while fast is not None and fast.next is not None:
            # Move slow pointer by one and fast pointer by two
            # When fast pointer reaches the end, slow pointer will be at the middle
            # If the list has an even number of elements, slow will point to the second middle
            slow = slow.next
            fast = fast.next.next
        print(f"Middle value: {slow.value}")
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
# new
# list1.push(11)
# list1.push(9)
# list1.push(6)
# list1.push(7)
# list1.push(8)
# list1.push(10)
# list1.printList()

list1.printMiddle() 

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        # Initialize head with a sentinel node
        self.head = Node('dummy')
        

    def push(self, new_data): 
        new_node = Node(new_data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return self.head
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        head = self.head
        slow = head
        fast = head
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

# Time Complexity - O(n)
# Space Complexity - O(1)
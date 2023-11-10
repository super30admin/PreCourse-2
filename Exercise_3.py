# Time Complexity - O(n/2)
# Space Complexity - O(1)

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
        if self.head == None:
            self.head = Node(new_data)

        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(new_data)
        
        return self.head
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head is None:
            return None
        
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
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

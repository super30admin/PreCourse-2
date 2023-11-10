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
        if self.head is None:
            self.head = Node(new_data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(new_data)

    # Function to get the middle of  
    # the linked list
    # Time complexity: O(n)
    # space complexity: O(1)
    def printMiddle(self):
        slow = fast = self.head
        while fast.next != None:
            fast = fast.next.next
            slow = slow.next
        print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle()

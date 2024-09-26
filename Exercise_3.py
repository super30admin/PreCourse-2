# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data = None):  
        self.val = data
        self.next = None
        
class LinkedList: 
    def __init__(self):
        self.tail = self.head = Node()
  
    def push(self, new_data):
        self.tail.next = Node(new_data)
        self.tail = self.tail.next
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        mid, end = self.head.next, self.head.next
        while end and end.next:
            mid = mid.next
            end = end.next.next
        return mid.val if mid else None

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(7) 
print(list1.printMiddle() )

'''
Time complexity: O(N)
Space complexity: O(1)
'''

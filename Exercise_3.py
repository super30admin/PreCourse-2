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
        temp = self.head
        newNode = Node(new_data)
        if temp is None:
            self.head = newNode
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slowPtr = self.head
        fastPtr = self.head
        while fastPtr.next is not None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        print(slowPtr.data)
        return slowPtr.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2)
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
# Time complexity: O(n)
# Space complexity: O(n); size of linked list

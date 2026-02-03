# Time complexity : O(n)
# Space complexity : O(1)

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
        newNode = Node(new_data)
        if self.head is None:
            self.head = newNode
        else: 
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Middle element :", slow.data)
        
# Driver code 
list1 = LinkedList()
list1.push(20)  
list1.push(50) 
list1.push(10) 
list1.push(30) 
list1.push(40) 
list1.push(70) 
list1.printMiddle() 
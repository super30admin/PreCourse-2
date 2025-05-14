# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
class LinkedList: 
  
    def __init__(self):
        self.head = Node(-1)
        
  
    def push(self, new_data): 
        curr = self.head.next
        if curr == None:
            self.head.next = Node(new_data)
            return
        while curr.next:
            curr = curr.next
        curr.next = Node(new_data)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow = self.head.next
        fast = self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        return


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

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
        temp = Node(new_data)
        curr = self.head
        if self.head is None:
            self.head = temp
            return
        while curr.next:
            curr = curr.next
        curr.next = Node(new_data)
   
    def printMiddle(self):
        slow = self.head
        fast = self.head
        if self.head is not None:
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next
            print("The middle element is -", slow.data)
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
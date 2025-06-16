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
        print("adding....")
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 

        #slow fast ptr method
        if not self.head or not self.head.next:
            return self.head

        slowPtr = self.head
        fastPtr = self.head.next
        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next

        return slowPtr.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle())


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
            nnode = Node(new_data)
            nnode.next = self.head
            self.head = nnode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 

        if self.head == None:
            print('LinkedList is empty')
            return

        slow = fast = self.head

        while True:
            if fast == None or fast.next == None:
                return print(slow.data)

            slow = slow.next
            fast = fast.next.next

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

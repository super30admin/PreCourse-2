# Node class 

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
    def __init__(self):
        self.head = None
        self.last = None

    def push(self, new_data): 
        if(self.head == None):
            self.head = Node(new_data)
            self.last = self.head
        else:
            self.last.next = Node(new_data)
            self.last = self.last.next

    # Function to get the middle of  
    # the linked list 
    def printLL(self): 
        ll = self.head
        while(ll!=None):
            print(ll.data)
            ll = ll.next
    
    def printMiddle(self):
        slow = self.head
        fast = self.head
        while(fast!=None and fast.next!=None):
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
print("Linked List: ")
list1.printLL()
print("Middle Element: ")
list1.printMiddle() 
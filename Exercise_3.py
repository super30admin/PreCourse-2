# Time complexity: O(n) ; n = no. of nodes
# Space complexity: O(1) ; space used by fast and slow pointer

# Node class  
class Node:  

    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None  

class LinkedList: 

    
    def __init__(self):
        self.head = Node(None)
        self.current = self.head 

    def push(self, new_data):
        #O(1)
        # #insert at start
        self.current.next = Node(new_data)
        self.current = self.current.next


    # Function to get the middle of  
    # the linked list 
    
    def printMiddle(self):
        #O(n/2)
        slow = self.head.next
        fast = self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Middle element: ", slow.data)
    
    def printlist(self):
        self.head=self.head.next
        while self.head:
            print(self.head.data)
            self.head=self.head.next


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()
list1.printlist()

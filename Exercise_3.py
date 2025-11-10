# Node class  
#TC is o(n) since the fast pointer moves thorugh all the elements
#SC is o(N) for pushing, and maybe constant for the finding part, since we use only two pointers
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
        newNode.next = self.head #push the earlier head as the next element of the new node to be added
        self.head = newNode #eastablish the new node as head
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow, fast = self.head, self.head #slow and fast pointer, bcz fast jumps twice as compared to slow, when the fast will be at the end, the slow will be in the mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print("Middle element:", list1.printMiddle().data) 

#SC o(n) for storing n elements

# Difficulty: Line 30 
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
  # TC = o(1) as it inserts at the front
    def push(self, new_data): 
        new = Node(new_data)
        new.next = self.head
        self.head = new
        print("Pushed",new_data)
  
    # Function to get the middle of  
    # the linked list 
    # TC Unsure if it's o(n) or o(n/2)
    def printMiddle(self): 
        slow = fast = self.head    # two pointer Rabbit and Tortoise method
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  # Does "next.next" skip the elements in between, if so, Can I take the TC as o(n/2)? as only n/2 elements would be traversed atmost.
        print("Middle element is:",slow.data)
        #return slow    
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

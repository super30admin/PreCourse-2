# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        # Dummy Node
        self.head = None
    
    # T: O(1), S: (1)
    def push(self, new_data): 
        # Add a new node to the front of the linked list
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        print(f"Pushed: {new_data}")
  
    # Function to get the middle of  
    # the linked list
    # Using Floyd's Tortoise and Hare Algo:
    # T: O(n), S: O(1)
    def printMiddle(self):
        s, f = self.head, self.head
        while f and f.next:
            s = s.next
            f = f.next.next
        print(f"Middle: {s.data}")



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
# list1.push(1) 
list1.printMiddle() 

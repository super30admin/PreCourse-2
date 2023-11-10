#time complexity : O(n)
#space complexity: O(1)
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
        newnode = Node(new_data)
        newnode.next = self.head
        self.head = newnode

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        node_fast = self.head
        node_slow = self.head
        while(node_fast != None and node_fast.next != None):
            node_slow = node_slow.next
            node_fast = node_fast.next.next
        print("The middle node's data is:", node_slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()

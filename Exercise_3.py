# Time Complexity: push is O(1), printMiddle is O(n), n is no.of elements in the linked list
# Space Complexity: O(1)

# Your code here along with comments explaining your approach




# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.counter = 0
        self.head = None
        self.tail = None
  
    def push(self, new_data):
        new_node = Node(new_data)
        
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        self.counter += 1
 
  
    # function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if not self.head:
            print("List is empty")
            return
        
        middle = self.counter // 2
        
        if self.counter % 2 == 0:
            middle -= 1
        
        middle_node = self.head
        i = 0
        
        while i < middle:
            middle_node = middle_node.next
            i += 1
        
        print(middle_node.data)
            
            
        
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

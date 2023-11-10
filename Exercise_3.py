# Time Complexity : O(n)
# Space Complexity: O(1)



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
        new_node = Node(new_data)
        if self.head == None : 
            self.head = new_node 
        else : 
            new_node.next = self.head 
            self.head = new_node
        
    def print(self):
        current = self.head
        while(current is not None):
            print(current.data)
            current = current.next
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        count = 0
        each = self.head 
        while  each.next is not None: 
            each = each.next 
            count += 1 
            
        size = count + 1 
        mid = (size + 1)//2
        each = self.head
        while mid > 1: 
            each = each.next
            mid -= 1 
        print(each.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
# list1.print()
list1.printMiddle() 

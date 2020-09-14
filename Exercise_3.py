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
        # Time Complexity : O(n)
        # Space Complexity : O(1) 
        newNode = Node(new_data)
        
        current_node = self.head
        while(current_node and current_node.next):
            current_node = current_node.next

        if(current_node):
            current_node.next = newNode    
        else:
            self.head = newNode 
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # Time Complexity : O(n/2)
        # Space Complexity : O(1) 
        current_node = self.head
        double_speed_node = self.head
        
        while(double_speed_node.next):
            current_node = current_node.next
            double_speed_node = double_speed_node.next.next

        if(current_node):
            print(current_node.data)
        else:
            print('')        


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

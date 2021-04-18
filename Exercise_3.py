"""
traverse the linked list and save the elements in an array and then find the mid.
Not the most optimal solution but it still works ;)

"""

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
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            new_node = Node(new_data)
            current_node.next = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 

        if self.head == None:
            return None
        else:
            current_node = self.head
            self.data = [current_node.data]
            while current_node.next:
                self.data.append(current_node.next.data)
                current_node = current_node.next
        
            mid = round(len(self.data)/2)
            print(self.data[mid])


        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

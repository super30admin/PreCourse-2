# Node class
# 
# Time Complexity = O(n)  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        
        self.head = None
  
    def push(self, new_data): 
                    
        node = Node(new_data)
        node.next = self.head
        self.head = node

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 

        temp1 = self.head
        temp2 = self.head

        while temp2 and temp2.next:
            temp1 = temp1.next
            temp2 = temp2.next.next

        print(temp1.data)

    def print(self):

        top = self.head
        while top!=None:
            print(top.data)
            top = top.next
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
# list1.print()
list1.printMiddle() 

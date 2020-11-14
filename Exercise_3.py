# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        self.size = 0
        
  
    def push(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
            self.size += 1
        else:
            current_node = self.head
            while(current_node.next != None):   #loop until last element is reached
                current_node = current_node.next

            current_node.next = Node(new_data)
            self.size += 1



  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        mid = int(self.size / 2)


        i = 0
        current_node = self.head
        while(i != mid):
            current_node = current_node.next
            i += 1
        print(current_node.data)




# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle() 

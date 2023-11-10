# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.value=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.length = 0
        self.tail = None 
  
    def push(self, new_data): 
        if self.head == None:       
            self.length = 1
            self.head = Node(new_data)
            self.tail = self.head
        else:                      
            self.length += 1
            present_node = Node(new_data)
            self.tail.next = present_node
            self.tail = present_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if (self.length % 2 != 0):      
            mid_id = int(self.length / 2)
            present_node = self.head
            cnt = 1
            while (cnt < mid_id):
                present_node = present_node.next
                cnt += 1
            print(present_node.next.value)

        else:                          
            mid_id = int(self.length / 2)
            present_node = self.head
            count = 1
            while (count < mid_id):
                present_node = present_node.next
                count += 1
            print(present_node.value, present_node.next.value)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

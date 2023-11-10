# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None  
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        self.len = 0
        self.tail = None
        
  
    def push(self, new_data):
        if self.head is None:
            self.len = 1
            self.head = Node(new_data)
            self.tail = self.head
        else:
            self.len += 1
            curr = Node(new_data)
            self.tail.next = curr
            self.tail = curr

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if (self.len %2 != 0):
            mid_id = int(self.len / 2)
            curr = self.head
            count = 1
            while (count < mid_id):
                curr = curr.next
                count += 1 
            print (curr.next.data)

        else:
            mid_id = int(self.len / 2)
            curr = self.head
            count = 1
            while(count < mid_id):
                curr = curr.next
                count += 1
            print (curr.data, curr.next.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

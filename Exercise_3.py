# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data,next):
        self.data = data
        self.next = next  
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data):
        #adding the data at the beginning  
        node = Node(new_data,self.head)
        self.head = node

    def find_length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head

        while itr:
            itr = itr.next
            count+=1  
        return count
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        count = self.find_length()
        middle = count // 2

        itr = self.head
        new_count = 0
        while itr:
            if(new_count == middle):
                print(itr.data)
                return
            itr = itr.next
            new_count+=1

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

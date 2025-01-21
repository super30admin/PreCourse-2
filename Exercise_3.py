# Time complexity: O(n)
# Space complexity : O(n) 

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.list_size = 0
  
    def push(self, new_data): 
        if self.head == None:
            self.head = Node(new_data)
            self.list_size += 1
        else:
            next_item  = self.head
            while next_item.next != None:
                next_item = next_item.next

            next_item.next = Node(new_data)
            self.list_size += 1

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        middle = self.list_size // 2
        next_item = self.head
        for i in (1, middle):
            next_item  = next_item.next
            i += 1

        print(next_item.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

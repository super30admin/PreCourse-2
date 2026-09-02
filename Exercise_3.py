# Node class  
class Node:  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList:   
    def __init__(self): 
        self.head = None
        self.tail = None
        self.length = 0
  
    def push(self, new_data): 
        new_node = Node(new_data)
        #  Edge cases, we add our first new_node
        is_first_node = self.length == 0
        self.length += 1

        if is_first_node:
            self.head = new_node
            self.tail = new_node
            return

        # Otherwise it is very standard
        self.tail.next = new_node
        self.tail = new_node
  
    # Function to get the middle of the linked list
    def printMiddle(self):
        middle = self.length // 2
        current = self.head
        for _ in range(middle):
            current = current.next

        print(f"middle node value: {current.data} - index: {middle}")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

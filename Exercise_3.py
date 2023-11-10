# Node class 
# Time complexity: O(n)
# space complexity: O(1) 
# Calculated the mid point using length of the linked list and then calculate the middle point and return that
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data =data
        
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
        count = 0
        start = self.head
        find = self.head
        while start:
            count += 1
            start = start.next
        middle = count // 2
        counter = 0
        while find:
            if counter == middle:
                return find
            else:
                find = find.next
        return None


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

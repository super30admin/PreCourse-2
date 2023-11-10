# Time Complexity: O(n)
# Space Complexity: O(n)

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
        newNode = Node(new_data)
        
        if self.head is None:
            self.head = newNode
            return 
        
        temp_node = self.head
        while(temp_node.next):
            temp_node = temp_node.next
        temp_node.next = newNode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        l = 0
        tmp_node = self.head

        while tmp_node is not None:
            l += 1
            tmp_node = tmp_node.next
        
        mid = int(l / 2)

        tmp_node = self.head
        while mid > 0:
            tmp_node = tmp_node.next
            mid -= 1

        print(tmp_node.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

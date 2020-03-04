# Node class  

## Time Complexity = O(1) for both insertion as well as for getting the middle element
## Space Complexity  =  O(N) to store the linked list . No auxillary space is used

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.val = data
        self.next = None
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.length = 0
        self.mid = None
  
    def push(self, new_data): 
        new_node = Node(new_data)
        self.length += 1
        if not self.head:
            self.head = new_node
            self.mid = new_node
            return
        self.head.next = new_node
        self.head = new_node
        if self.length%2==1:
            self.mid=self.mid.next
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.mid:
            print(self.mid.val)
        else:
            print(None)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

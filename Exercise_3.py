# Time Complexity : O(N)
# Space Complexity : O(1)

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
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        return self.head
    
    def getLen(self, head):
        temp = head
        len = 0
 
        while (temp != None):
            len += 1
            temp = temp.next
 
        return len
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head != None:
            
            len = self.getLen(self.head)
            temp = self.head
            
            midIdx = len // 2
            while midIdx != 0:
                temp = temp.next
                midIdx -= 1
            print("Middle element is: [%d]" % temp.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

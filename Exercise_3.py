# Time Complexity : O[n]
# Space Complexity : O[1]
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
        node = Node(new_data)
        if self.head is not None:
            node.next = self.head
        self.head = node
        curr = self.head
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head is None:
            print(-1)
        else:
            fast = self.head
            slow = self.head
            i = 0
            while fast is not None:
                fast = fast.next
                i+=1
                if i%2==0:
                    slow = slow.next
            print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

# Time Complexity :O(N)
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
        n = Node(new_data)
        n.next = self.head
        self.head = n
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # 2 pointer method
        p1 = self.head # slow
        p2 = self.head # fast

        while p2 is not None and p2.next is not None:
            # even length
            if p2.next.next is None:
                print(p1.data)
                return
            
            p1 = p1.next
            p2 = p2.next.next
        
        print(p1.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

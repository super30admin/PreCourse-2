# Time complexity = O(n)
# Space complexity = O(1)


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
        newNode.next = self.head
        self.head =  newNode
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if(not self.head):
            print("List is empty")

        slow, fast = self.head, self.head

        while(fast.next):
            slow = slow.next # slow pointer moves one step
            fast = fast.next.next # fast pointer moves 2 steps
        print(slow.data)

# Driver code 
list1 = LinkedList()

list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

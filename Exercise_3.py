# Node class  
#  Time complexity push O(1) middle -o(n)
# space o(n)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.next = None
        self.data = data 
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.size = 0
  
    def push(self, new_data):
        if not self.head:
            newNode = Node(new_data)
            self.head = newNode
            self.size+=1
            return self.head
        newNode = Node(new_data)
        curr = self.head
        while curr.next:
            curr=curr.next
        curr.next = newNode
        self.size+=1
        return self.head

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if not self.head or self.size == 0 :
            print("No middle linkedList empty") 
            return

        middle = (self.size)//2
        curr = self.head
        for i in range (1,middle+1):
            curr = curr.next
        print(curr.data)

        



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

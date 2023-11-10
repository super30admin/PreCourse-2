# Time Complexity: O(n)

# Space COmplexity: O(1)

class Node:  
   
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None
class LinkedList: 
  
    def __init__(self):
        self.head=None 
        
    def push(self, new_data):       #inserting at last
        newNode=Node(new_data)
        if self.head:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=newNode
        else:
            self.head=newNode

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head:
            middle=self.head
            if self.head.next:
                while(self.head.next and self.head.next.next):
                    middle=middle.next
                    self.head=self.head.next.next
        print(middle.data)
                    
                
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

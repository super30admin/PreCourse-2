#Time complexity : O(n)
#Space complexity : O(1)


# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None #initialize head
  
    def push(self, new_data): # insert new node at the start
        new = Node(new_data)
        new.next = self.head
        self.head = new
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # two ponters, slow wll move 1 step and fast will move 2 steps
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.data)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

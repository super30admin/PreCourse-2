# Node class
#Time Complexity push -> O(1) middle -> O(n/2) -> O(n)
#Auxilary Space Complexity O(1)
# incrementing size variable by whenever a push happens and mid will at the half of the size
# parse through the linked list for those number of times
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.size = 0
        self.tail = None
  
    def push(self, new_data): 
        if self.head == None:
            self.head = Node(new_data)
            self.tail = self.head
            self.size += 1
            return;
        self.tail.next = Node(new_data)
        self.tail = self.tail.next
        self.size += 1
        return;
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head == None:
            print("Empty LinkedList")
            return None;
        if self.size % 2 == 0:
            i = 0
            pres = self.head
            while i < (self.size//2) -1:
                pres = pres.next
                i += 1
            print(pres.data)
            print(pres.next.data)
        else:
            i = 0
            pres = self.head
            while i < self.size//2:
                pres = pres.next
                i += 1
            print(pres.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

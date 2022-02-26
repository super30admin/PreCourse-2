# Time Complexity -> O(n) to add n elements and to find the middle element -> O(n/2)
#Space complexity -> O(n)


# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        #self.count = 0
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.count = 0

  
    def push(self, new_data): 
        if self.head == None:
            node = Node(new_data)
            self.head = node
            self.count += 1

        else:
            node = Node(new_data)
            self.count += 1
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        current = self.head
        mid = self.count // 2
        i = 0
        while i != mid:
            i += 1
            current = current.next
        print(current.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

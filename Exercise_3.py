#Space Complexity: O(n) ... where n is the number of elements
#Time Complexity: O(n) ... where n is the number of elements
#The code did run successfully

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
        if self.head:                               #appending the new node by first iterating through the entire linked list
            iter = self.head
            while iter.next:
                iter = iter.next
            new_node = Node(new_data)
            iter.next = new_node
        else:
            self.head = Node(new_data)              #when the linked list is empty, adding the new node as it is
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):                          #iterating through the entire linked list to determine the length of it
        iter = self.head
        length = 1
        while iter.next:
            length += 1
            iter = iter.next
        print("length: ",length)
        
        ptr_count = 0
        ptr = self.head
        while ptr.next:
            if ptr_count == length//2:              #iterting till we reach the middle element
                print("middle element: ",ptr.data)
                return
            ptr_count += 1
            ptr = ptr.next

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

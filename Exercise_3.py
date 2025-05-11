# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None, next=None):  
        self.value = data
        self.next = next
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        node = Node(new_data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head is None:
            print("Linked List is Empty")
        counter = 0
        iter = self.head
        mll = self.head
        while iter:
            print(f" -> ", end=" ")
            print(f"{iter.value}", end=" ")
            iter = iter.next
            counter+=1
            if counter % 2 == 0:
                mll = mll.next
        
        print(f"the middle node is {mll.value}") 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(6) 
list1.push(9) 
list1.push(15) 
list1.push(3) 
list1.printMiddle() 

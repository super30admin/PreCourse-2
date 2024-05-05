# Status : Completed 
# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data=None, next = None ):  
        self.data = data 
        self.next = next  

class LinkedList: 
  
    def __init__(self): 
        self.head = None 
  
    def push(self, new_data): 
        newnode = Node(new_data)

        if self.head==None:
            self.head = newnode 
            return newnode

        curr = self.head 
        while curr.next!= None: 
            curr = curr.next 
        curr.next = newnode
        return newnode

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        curr = self.head 
        fastPtr = self.head 
        head = self.head

        if head.next == None :
            print("Empty")
            return head 

        head_next  = head.next 
        if head_next.next == None :
            print(self.head.data)
            return self.head
        else:
            fastPtr = head_next.next       

        # depends on whether we have even or odd number list 
        while (1): 
            if fastPtr.next==None: 
                print(curr.next.data)
                return curr.next 
            if fastPtr.next.next==None:
                print(curr.next.data)
                return curr.next
            curr = curr.next 
            fastPtr = fastPtr.next.next 
           



# Driver code 

list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print("Middle1")
list1.printMiddle() # 5 4 2 3 1 
print("Pushing")
list1.push(6)
print("Middle2")
list1.printMiddle()  # 5 4 2 3 1 6
list1.push(7)
list1.push(8)
list1.push(9)
print("Middle3") # 5 4 2 3 1 6 7 8 9
list1.printMiddle() 

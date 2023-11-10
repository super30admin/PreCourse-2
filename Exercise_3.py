# Node class  
# // Time Complexity : O(n)
# // Space Complexity : O(1)

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
        self.head = newNode

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        ptr1 = self.head
        ptr2 = self.head
        if self.head is not None:
            while ptr1 is not None and ptr1.next is not None:
                ptr1 = ptr1.next.next
                ptr2 = ptr2.next
            print("Middle Element is", ptr2.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()
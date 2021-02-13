
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
        new_node = Node(new_data)
        if self.head == None:
            print('LikedList is Empty, will add directly')
            self.head = new_node

        else:
            print('Linkedlist not empty, adding new element')
            n = self.head
            while n.next != None:
                n = n.next
            n.next = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        i = 0
        j = 0
        n = self.head
        while n.next != None:
            n = n.next
            i +=1
        n.next = self.head.next
        while n.next != None and j < (i//2):
            n = n.next
            j +=1
        print("Mid Point is", n.data)

        return n.data
# Driver code 
list1 = LinkedList() 
list1.push(10)
list1.push(98)
list1.push(50)
list1.push(30)
list1.push(20)
list1.printMiddle() 

#Time Complexity : O(n)
#Space Complexity : O(1)
#This code runs fine with desired output


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
        if self.head == None:
            self.head = Node(new_data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(new_data)

    def printSLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        #creating two pointers for to travers the linkedlist
        fast = self.head #increament by 2 nodes
        slow = self.head #increament by 1 node

        while fast.next is not None:
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
# list1.push(0)
# list1.push(-1)
# list1.printSLinkedList()
list1.printMiddle()

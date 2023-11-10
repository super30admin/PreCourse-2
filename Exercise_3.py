#Time Complexity: O(n)
#Space Complexity: O(1)

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): # create a node with data and next
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):  # create a head pointer
        self.head = None
  
    def push(self, new_data): 
        newNode = Node(new_data)

        if self.head == None: # if the list is empty the new node is the head
            self.head = newNode
        
        else: # travel to the end of the list and append the new node
            point = self.head
            while point.next:
                point = point.next
            point.next = newNode

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        dummy = self.head #get dummy pointer to start of two pointers

        slow = dummy
        fast = dummy

        while fast.next and fast.next.next: # fast travels two steps and slow travels one. 
            slow = slow.next
            fast = slow.next
        return slow.data # return the slow pointer data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()

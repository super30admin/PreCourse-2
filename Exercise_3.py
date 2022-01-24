
#Time Complexity: O(n) as there is a while loop for traversing in the whole loop
#Space Complexity: O(1) 
# this code is tested on Python editor 

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data= data # for storing the data of the node
        self.next= None # to point to its next location.
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        temp = self.head
        node = Node(new_data)  # creating the node for insertion
        if temp is None: 
            self.head = node # Insertion if the LinkedList 
        else:
            while temp.next is not None:
                temp = temp.next  
            temp.next= node # insertion at the end of the list.
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        #we will use 2 pointer approach
        fast = self.head # we will increment 2 times
        slow = self.head # this will increment only one time
        while fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        print(slow.data)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

#Time Complexity: O(n) as there is a while loop for traversing in the whole loop
#Space Complexity: O(1) 
# this code is tested on Python editor 
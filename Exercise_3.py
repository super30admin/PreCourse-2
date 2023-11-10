
# // Time Complexity : O(N)for push and O(log n) for printmiddle?
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this :no


# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.counter=0                  #keeping a counter to get the length of the linked list
        
  
    def push(self, new_data): 
        top = self.head
        if(self.head == None):
            self.head = Node(new_data)
            self.counter+=1
        else:
            while(top.next !=None):
                top = top.next
            top.next = Node(new_data)
            self.counter+=1
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        i=1
        top= self.head
        while(top!=None):
            if (i==(self.counter//2)+1):            # if you get to the node that is (half +1 of the length of the linkedlist) i.e the middle of the linkedlist, print the data
                print(top.data)
            top=top.next
            i+=1



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

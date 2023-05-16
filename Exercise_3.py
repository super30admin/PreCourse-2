#Time complexity is O(n), where n is the number of elements in the linkedlist
#Space complexity is O(1) Node and LinkedList
#Code ran successfully on leetcode terminal
#I faced no problems while implementing the code
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        #assigning values to self.data and self.next
        self.data=data
        self.next=None  
        
class LinkedList: 
  
    def __init__(self):
        #Assigning intial values to head and length
        self.head=None
        #here we are creating length to find the size of the linked list 
        self.length=0 
        
    def push(self, new_data):
        #if we are inserting the first value to linked list the code in the 'if' part gets executed
        if(self.head==None):
            self.head=Node(new_data)
            self.length+=1
        #if there are existing values in linked list, we will be adding them to the last.
        else:
            value=self.head
            while(value.next):
                value=value.next
            #Adding the new value at the end of the linked list
            value.next=Node(new_data)
            self.length+=1
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # we are dividing the length value by 2 to get the middle postion
        middle=self.length//2
        position=self.head
        #We will be using while loop to go the middle position
        while(middle>0):
            position=position.next
            middle-=1
        #we are going to print the data in the middle position
        print(position.data)
        
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()

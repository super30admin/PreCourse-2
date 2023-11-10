# Time Complexity : O(n) where n stands for number of nodes in the linked list
# Space Complexity : O(1) since there is no extra space used
# Did this code successfully run on Leetcode : Did not try running code on leetcode as the question and inputs on leetcode are bit different.
# Any problem you faced while coding this : Had issues while writing the printMiddle() later found out the logic by using length of linked list

# Your code here along with comments explaining your approach

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data                    #Initialized data and next pointers
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = None                    #initialized head pointer to None
  
    def push(self, new_data):
        newNode = Node(new_data)            #create NewNode of type Node
        newNode.next = self.head            #set head to be the next node of new node
        self.head = newNode                 #change pointer of head pointing to the new node
        return self.head
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        length = 0                          #get length of current linked list
        curr = self.head
        while curr:
            length += 1                     #incrementing length value
            curr = curr.next

        curr = self.head                    #reset curr pointer to head
        middleIndex = length//2             #compute the middle index by length//2
        while middleIndex:                  #iterate over the input until we reach middle and decrement middle index by 1 every iteration
            curr = curr.next
            middleIndex -= 1

        print(f"The middle element is: {curr.data}")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

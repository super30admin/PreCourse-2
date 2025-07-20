#Time Complexity :O(n)
#Space Complexity :O(1)
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : none
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None  # empty Linked list 
        
  
    def push(self, new_data): 
        new_node=Node(new_data)     # create a new node to be added to the list
        new_node.next=self.head     # the new node is added at the beginning and next points to the previously exisitng linked list
        self.head=new_node          # the beginning of the linked list is the new node 
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        count = 0                    # keep a count of the number of the elements 
        curr_node=self.head          # start from the beginning
        while curr_node:             # while there are still elements in the list
            count=count+1            # increment the counter
            curr_node=curr_node.next
        mid=count//2                 # get the mid value 
        curr_node=self.head
        for j in range(mid):
            curr_node=curr_node.next  # traverse to the mid value
        
        if curr_node:                 # if the middle element is not none print it 
            print("The middle element in the linked list is" ,curr_node.data)
        else:
            print("Empty")            # else print empty

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

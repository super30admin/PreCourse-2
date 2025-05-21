#Time Complexity : O(n) - first pass to count nodes and second pass to reach the middle takes O(n)
#Space Complexity :O(1) - as no extra data structures 
#Did this code successfully run on Leetcode : yes

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data=data
        self.next=None 
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
  
    def push(self, new_data): 
        new_node=Node(new_data)
        new_node.next=self.head #new node points to the current head of the list 
        self.head=new_node #updates the lists head to the new node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        count=0
        temp=self.head

        while temp: #loops as long as temp is not none
            count +=1
            temp=temp.next
            #count holds the total number of nodes
        mid_index=count//2 

        current=self.head
        for _ in range(mid_index):
            current = current.next

        if current:
            print("The Middle element is:", current.data)
        else:
            print("The list is empty.")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

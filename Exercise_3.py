# Time Complexity : O(N) to print, N being the number of nodes.  
# Space Complexity : O(N), N being the number of nodes. 
# Did this code successfully run on Leetcode : Yes, it did. 
# Any problem you faced while coding this : Forgot the line 
# "self.end = self.end.next" and had to figure out why there 
# were not values in the middle. 


# Your code here along with comments explaining your approach

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
    
    def __init__(self): 
        self.linked_list = Node(None)
        self.end = self.linked_list
  
    # Push while keeping and saving the end node. 
    def push(self, new_data): 
        if self.linked_list.data == None:
            self.linked_list = Node(new_data)
            self.end = self.linked_list
        else:
            self.end.next = Node(new_data)
            self.end = self.end.next

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        #assumes an odd number of nodes. 
        mid = self.linked_list
        end = self.linked_list
        # while mid is traversed once, end is traversed two times.
        # mid will then be in the middle if odd number of nodes. 
        while(end!=None):
            end = end.next
            if end!=None:
                end = end.next
            else:
                break
            mid = mid.next
        print(mid.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

# Node class 
#// Time Complexity : O(n)
# // Space Complexity :O(n)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this :No


# // Your code here along with comments explaining your approach
# In print middle, we start with array with head in it.
# we add nodes to this array is we travel
# once we have all the elements we return the middle element by returning arr[l+(r-l)] // 2
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.next = None
        self.data = data 
        
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
        return self.head

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        arr = [self.head]
        temp = self.head.next
        while temp is not None:
            arr.append(temp)
            temp = temp.next
        print((arr[len(arr)//2]).data)


# Driver code 
list1 = LinkedList()
list1.push(1) 
list1.push(2) 
list1.push(3) 
list1.push(4) 
list1.push(5) 
list1.printMiddle() 

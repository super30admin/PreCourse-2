# // Time Complexity : O(n) - depends on the size of the list
# // Space Complexity : O(1) - only new pointers are initialized
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None 

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.next = None
        self.data = data
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None 
        
    def push(self, new_data):
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode
    
    def printElems(self):
        temp = self.head
        while temp:
            print(f"{temp.data}->", end="")
            temp = temp.next
        print("None")
        
    def sizeList(self):
        temp = self.head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        return size
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        count = self.sizeList() // 2
        temp = self.head
        for i in range(0, count + 1):
            if i == (count):
                return temp.data
            else:
                temp = temp.next
            
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printElems()
print(list1.printMiddle())

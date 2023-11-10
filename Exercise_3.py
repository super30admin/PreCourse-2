'''
Approach
1. Complete th filler methods for node and push
2. In print middle, perform floor division for length of linked-list and store it in mid variable
3. Maintain currentNode that refers the linked-list from the beginning
4. Move the currentNode rfr to the next node and decrease the mid by -1. Peform this in a loop
5. Return the currentNode.value which will be the middle of linked-list
6. Time Complexity: 0(n/2) equivalent to 0(n)
   Why: We are scanning till the middle of linked-list
'''
# Node class  
class Node:  
    
    # Function to initialise the node object  
    def __init__(self, data):  
        self.value = data
        self.next = None
    
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, new_data): 
        # 1. Create a new node object
        objNewNode = Node(new_data)
        
        if self.length == 0:
            self.head = objNewNode
            self.tail = self.head
        
        else:
            self.tail.next = objNewNode
            self.tail = objNewNode
        
        self.length +=1
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        mid = self.length // 2
        
        if mid == 0:
            # Only 1 element in the list
            return self.head.value
        
        else:
            # Iterate till mid is -1
            currentNode = self.head
            
            while mid >0:
                currentNode = currentNode.next
                mid -=1
                continue
            
            return currentNode.value
    
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()
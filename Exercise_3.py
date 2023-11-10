# Node class  
# Time complexity O(n)
# Space complexity O(1) Constant Space

class Node:  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next=None

class LinkedList: 
  
    def __init__(self,node=None): 
        self.node = node
        self.size = 0
        
  
    def push(self, new_data):
        if self.node == None:
            self.node = Node(new_data)
            self.size +=1
            return
        temp = self.node
        while temp.next !=None:
            temp = temp.next
            
        temp.next = Node(new_data)
        self.size +=1

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.node == None:
            print("No element in the list")
            return

        temp = self.node

        for x in range(0,(self.size//2)):
            temp = temp.next
        print("Middle Element = "+ str(temp.data))
        
        pass

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)  
list1.printMiddle()
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data): 
        if self.head == None:
            self.head = Node(new_data)
        else :
            temp = Node(new_data)
            temp.next = self.head
            self.head = temp 
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        l1 = self.head
        l2 = self.head
        count = 0
        while l1.next != None :
            l1 = l1.next
            #temp = l1.next
            count = count + 1
            

           # return l1.data
        if count%2 == 2:
            count = count/2
        else:
            count = 1 + count//2 

        #print(count)
        while count > 1:
            count = count -1
            l2 = l2.next
            
        print(l2.data,"middle element")



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
 

list1.printMiddle() 

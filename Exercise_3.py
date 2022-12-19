#Time Complexity :
# O(N)

#Space Complexity :
# O(N)

#Did this code successfully run on Leetcode :
#Yes

#Any problem you faced while coding this :
#No

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
        if self.head == None :
            self.head = Node(new_data)
        else : 
            current = self.head
            while current.next != None :
                current = current.next
            current.next = Node(new_data)
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        current = self.head
        count = 0
        if current == None :
            print ("None")
            return
        elif current.next == None :
            print (head.data)
            return
        else:
            while (current.next) != None :
                current = current.next
                count += 1
            count += 1

        new_current = self.head
        for i in range(0,int(count/2)):
            new_current = new_current.next
        print (new_current.data)
        return
            

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(1) 
list1.push(1) 
list1.push(1) 
list1.push(1) 
list1.printMiddle() 

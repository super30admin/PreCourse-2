# Node class
# Time Complexity 0(n2)

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
          self.data = data
          self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        # self.next = None
  
    def push(self, new_data):
        print(new_data)
        newnode = Node(new_data)
        if(self.head == None):

            self.head = newnode
     
        else:
            newnode.next = self.head
            self.head = newnode
            

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
  
        current =self.head
        counter = 0
        while current!=None:
        
            counter+=1
            current = current.next
        i =0
        middle = self.head
        while(i<=counter and middle!=None):
            if(i!=counter):
                middle=middle.next
            else:
                return middle.data


            


        print(counter//2)
      

# Driver code 
list1 = LinkedList() 
list1.push(6) 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

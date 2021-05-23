# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None):
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self):
        self.head=Node(None)

        
  
    def push(self, new_data):
        current=self.head

        if(self.head.data==None):

            self.head.data=new_data
        else:

            while current.next!= None:
                current=current.next

            current.next=Node(new_data)
            return

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
            count=1
            current = self.head


            while current.next!= None:
                current = current.next
                count+=1
            current = self.head
            for i in range(int(count/2)):
                current=current.next
            print(current.data)


            return current



        # Driver code
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

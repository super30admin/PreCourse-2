# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, value):
        self.value=value
        self.link=None
        
class LinkedList: 
  
    def __init__(self):
        self.start=None
  
    def push(self, new_data):
        new_node=Node(new_data)
        curr=self.start
        if curr==None:
            self.start=new_node
        else:
            while curr.link!=None:
                curr=curr.link
            curr.link=new_node

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow=self.start
        fast=self.start
        while fast!=None:
            if fast.link == None:
                break
            fast=fast.link.link
            slow=slow.link
        print(slow.value)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle() 

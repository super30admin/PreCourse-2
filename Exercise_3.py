# Node class  
class Node:  
    def __init__(self, data):  
        self.data=data
        self.next=None
class LinkedList: 
  
    def __init__(self): 
        self.length=1
        self.root=Node(-1)
        self.cur=self.root
    def push(self, new_data): 
        node=Node(new_data)
        self.cur.next=node
        self.cur=self.cur.next
        self.length+=1
        
    def printMiddle(self):
        if self.length==1:
            return None
        midpoint=(self.length-1)//2
        self.findNode=self.root.next
        while(self.findNode!=None and midpoint>0):
           midpoint-=1
           self.findNode=self.findNode.next
        print(self.findNode.data)

           
           

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4)
list1.push(2)
list1.push(3) 
list1.push(1)
list1.printMiddle() 

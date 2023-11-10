# Node class  
# Time Complexity: O(n)
# Space Complexity: O(1)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data=data
        self.next=None 
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
  
    def push(self, new_data): 
        newNode=Node(new_data)
        if self.head==None:
           self.head= newNode
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=newNode
  
    def show(self):
        printList=""
        if self.head==None:
            print("List is Empty")
        else: 
            n=self.head
            while n is not None:
                printList+=str(n.data)+"->"
                n=n.next
            print("Linked List: ",printList)

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head==None:
            print("List is Empty")
        else: 
            n=self.head
            q=self.head
            count=0
            while n is not None:
                count+=1
                n=n.next
            print("Count of nodes",count)

            mid=int(count/2)
            
            print("Mid Index",mid)

            for i in range(0,mid):
                q=q.next
            print(q.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(7) 
list1.push(3) 
list1.push(1) 

list1.show()

list1.printMiddle() 

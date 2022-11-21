# Node class
#Time Complexity O(n)
#Space Complexity O(n)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self):
        self.head=None
        self.tail=None
        
  
    def push(self, new_data): 
        if self.head==None:
            self.head=Node(new_data)
            self.tail=self.head
        else:
            # new_node=Node(new_data)
            self.tail.next=Node(new_data)
            self.tail=self.tail.next

  
    # Function to get the middle of  
    # the linked list 
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' -> ')
            temp=temp.next
        print()

    def printMiddle(self):
        # declaring two variable one move twice faster than the other one so faster one reaches the end of the linked list by the time second reaches mid point.
        slow=self.head
        fast=self.head
        try:
            while(fast.next.next):
                slow=slow.next
                fast=fast.next.next
        except:
            pass
        finally:
            print('Mid Point of the Linked list',slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(0)
list1.push(-1)
list1.printlist()
list1.printMiddle()

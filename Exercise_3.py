# Time Complexity: O(n)
# Space Complexity: O(1)
# Node class  
class Node:  
    
    # Function to initialise the node object  
    def __init__(self, data):
        self.data=data
        self.next=None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
        self.tail=None
        self.count=0
  
    def push(self, new_data): 
        nn= Node(new_data)
        if self.head is None:
            self.head=self.tail=nn
        else:
            self.tail.next=nn
            self.tail=nn
        self.count+=1

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        c=-1
        n=self.head

        if n is None:
            print("Empty List")
            return 
        else:
            while c < self.count//2:
                c+=1
                if c==self.count//2:
                    break
                n=n.next
            print("Middle element is", n.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(7)
list1.push(9) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

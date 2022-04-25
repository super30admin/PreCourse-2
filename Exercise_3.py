# Node class  
from hashlib import new


class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next


class LinkedList: 

    def __init__(self): 
        self.head = None


    def push(self, new_data): 
        if self.head is None:
            self.head = Node(new_data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(new_data)


    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head is None:
            print("LL is empty")
        else:
            itr = self.head
            count = 0
            while itr:
                count += 1
                itr = itr.next
            count = count // 2
            a = 0
            itr = self.head
            while itr:
                if a == count:
                    return itr.data
                itr = itr.next
                a += 1

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(100) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle())

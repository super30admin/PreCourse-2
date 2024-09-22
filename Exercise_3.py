class Node:  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data
        self.next = None
        
class LinkedList: 
    def __init__(self):
        self.head = None
        self.len = 0
        
    def push(self, new_data): 
        newNode = Node(new_data)
        if self.head == None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newNode
        self.len += 1
    
    def showLL(self):
        if self.head == None:
            print("Empty")
        else:
            curr = self.head
            ll = ''
            while curr != None:
                ll = ll + str(curr.data) + " -> "
                curr = curr.next
            print(ll[:-4])
            
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        print("Total Elements = ", self.len)
        curr = self.head
        middle = int((self.len + 1)/2)
        i = 1
        print("Middle: ")
        if self.len % 2 != 0:
            while i != middle:
                curr = curr.next
                i += 1
            print(curr.data)
            return curr.data
        else:
            while i != middle:
                curr = curr.next
                i += 1
            mid1 = curr.data
            mid2 = curr.next.data
            print(mid1, mid2)
            return mid1, mid2 
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

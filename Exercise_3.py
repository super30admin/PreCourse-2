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
        #Inserts new node at the beggining
        #Space complexity: O(1)
        #Time complexity : O(1)
        newnode = Node(new_data)
        newnode.next = self.head
        self.head = newnode
        
    # Function to get the middle of  
    # the linked list 
    #Space complexity: O(1)
    #Time complexity : O(n)
    def printMiddle(self): 
        #If empty list
        if self.head is None:
            return None
        current = self.head
        #slow pointer moves one step while fast pointer moves 2 steps at a time
        slow = current
        fast = current
        #we iterate till fast reaches the end
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data # since slow now points to middle node

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle())

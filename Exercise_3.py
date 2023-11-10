"""
Time Complexity : O(n)
Space Complexity : O(1) recursive call
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this :no


Your code here along with comments explaining your approach

"""

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self._size = 0
        
  
    def push(self, new_data): 
        node = Node(new_data)
        self._size +=1

        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
        node.next = None


            
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head == None:
            return 
        curr = self.head
        count = 0
        mid = (0 + self._size)//2
        print(mid)
        while curr and (count != (self._size//2)) :
            curr = curr.next
            count +=1

        return curr.data

    def printMiddle_2(self):
        """
        if the size of the linked list is not given
        """
        if head==None:
            return
        length = 0
        curr = head
        while curr is not None:
            length +=1
            curr = curr.next
            
        for _ in range(length//2):
            head = head.next
            
        return head
    

            

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.print_list()

list1.printMiddle() 

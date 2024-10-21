# // Time Complexity : O(n) printMiddle iterates
# // Space Complexity : O(1) only 2 pointes to take up space
# // Did this code successfully run on Leetcode :NA
# // Any problem you faced while coding this : Kept failing with bruteforce found this out.
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
        node = Node(new_data)       #node(data, next) add data to LL
        node.next = self.head
        self.head = node
  

    # def printLL(self): 
    #     while self.head is not None:
    #         print(self.head.data, end = " ")
    #         self.head = self.head.next
    #     print()

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow = self.head            
        fast = self.head

        while fast and fast.next:
            slow = slow.next            #moves at 1x speed
            fast = fast.next.next       #moves at 2x speed
        print(slow.data)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
# list1.printLL() 
list1.printMiddle() 

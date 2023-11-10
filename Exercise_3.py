# Node class  
#time complexity=   O(N)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data
        self.next = None 
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        ptr1= self.head
        ptr2= self.head

        if self.head is not None:
            while(ptr1 is not None and ptr2.next is not None):
                ptr2= ptr2.next.next
                ptr1= ptr1.next
            print('Mid point: ', ptr1.data)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 


#The solution I have implemented on Leetcode: Please take a look.
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#             temp =  head
#             len = 0
 
#             while temp:
#                 len += 1
#                 temp = temp.next
#             midIdx = len // 2
            
#             new_node=head
#             for i in range(midIdx):
#                 new_node=new_node.next
#             return new_node
            
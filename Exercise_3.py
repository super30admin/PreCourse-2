'''
Time Complexity: 
    1) push: O(1)
    2) printMiddle: O(N/2) ~ O(N), N=size of LinkedList
Space Complexity: 
    1) Constant for APIs. 
    2) O(N) for storage of N nodes in list
'''

# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data=None):  
        self.data = data
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.root = Node()
        self.curr = self.root
    def push(self, new_data): 
        new_node = Node(new_data)
        self.curr.next = new_node
        self.curr = new_node        
  
    # Function to get the middle of  
    # the linked list 
    
    def printMiddle(self):
        slow = self.root
        fast = self.root
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        return slow



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

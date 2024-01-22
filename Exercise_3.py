# Node class 
#Time Complexity: O(1) for pushing the element on the stack, O(n) to print middle element of linked list.
#Space Complexity O(1)  for both pushing element onto stack and to print middle element of linked list.
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList: 
  
    def __init__(self):
        self.head = Node(0) 
        
  
    def push(self, new_data):
        #Assuming this is stack push function
        stack = self.head.next # here head is a null node
        newNode = Node(new_data)  
        self.head.next = newNode
        newNode.next = stack # make next of the new node point to the first node in the linked list
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        #create slow and fast pointers
        slowPtr = self.head
        fastPtr = self.head
        while slowPtr.next!=None and fastPtr.next!=None and fastPtr.next.next!=None:
            #make the slow pointer traverse one node per iteration, the fast pointer traverse two nodes per iteration
            # print(f"slowPtr is at {slowPtr.data} and fastPtr is at {fastPtr.data}")
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        print(f"The middle is {slowPtr.data}")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

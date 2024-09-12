# Node class  
# Time Complexity : O(n)
# Space Complexity : O(n)
# Any problem you faced while coding this : No
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.mid = 0
        self.head = None 
  
    def push(self, new_data): 
        newNode = Node(new_data)
        if (self.head is None):
            self.head = newNode
        else:
            temp = self.head
            while (temp.next!=None):
                temp = temp.next
            temp.next = newNode
  
    # Function to get the middle of  
    # the linked list 
    # There can be 2 ways to solve this coding problem, one would be simply iterating over the linkedlist copying into array and then finding mid elelemnt.
    # To avoid using extra space I used the 2 pointer approach, initially both pointers are at head of list and then I move ptr1 by 1 and ptr2 by 2 positions.
    # In this way, when the ptr2 reaches the end of list the ptr1 will be pointing to middle of  linkedlist.
    def printMiddle(self):
        ptr1 = self.head
        ptr2 = self.head
        if ptr1 is None or ptr2 is None:
            print("Empty linked list")
            return
        if (ptr1.next is None or ptr2.next is None or ptr1.next.next is None or ptr2.next.next is None):
            print("Middle of linked list is at element: ",ptr1.data)
            return ptr1
        else:
            while(ptr2.next!=None):
                ptr1 = ptr1.next
                ptr2 = ptr2.next.next
            print("Middle of linked list is at element: ",ptr1.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

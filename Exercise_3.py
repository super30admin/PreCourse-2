# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.root = None
        
    def push(self, new_data):
        if not self.root:
            self.root = Node(new_data)
        else:
            temp = Node(new_data)
            temp.next = self.root
            self.root = temp

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.root
        fast = self.root
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow.data


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(7) 
list1.push(10)
print("Middle Elemenet is:",list1.printMiddle())

#TC: O(n) we traverse the linkedlist with 2 pointers at the same time
# SC: O(1) we do not need extra space to find the middle element
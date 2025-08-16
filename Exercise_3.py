#Time Complexity: O(N) because we traverse the wholedata
#Space Complexity: O(1) because we have use of two pointers slow and fast
#Approach: Two pointer approach also called as the slow and fast pointer approach the famous hare and tortoise problem

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head =None
        
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head= new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # Initialize the slow and fast pointer 
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            # Move the fast pointer by two nodes
            fast = fast.next.next
            # Move the slow pointer by one node
            slow = slow.next
        # middle node of the linked list
        print(f"This is the middle of the linked list {slow.data}")
        return slow.data
        

if __name__ == "__main__":  

# Driver code 
    list1 = LinkedList() 
    list1.push(5) 
    list1.push(4) 
    list1.push(2) 
    list1.push(3) 
    list1.push(1) 
    list1.printMiddle() 

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
    
    # Pushing an element to the end of the LL. Takes O(n) time to go to the end and add a new node.
    def push(self, new_data): 
        if self.head is None:
            self.head = Node(new_data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(new_data)

    # Function to get the middle of LL. Time complexity is O(n). One iteration to go over the whole list and another iteration to print the middle element. Therefore the total is O(n) + O(n) = O(n)
    def printMiddle(self): 
        count = 0
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            count += 1
        count = int((count+1)/2) # We add one to account for the last node (whose next pointer is null)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            count -=1
            if count == 0:
                print(temp.data)
                break


# Driver code 
list1 = LinkedList() 
list1.push(6) 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.printMiddle() 
list1.push(1) 
list1.printMiddle() 

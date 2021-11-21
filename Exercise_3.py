# Node class  
#Time Complexity - O(n)
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
        if self.head is None:
          self.head = new_node
          return
        current_node = self.head
        self.head = new_node
        self.head.next = current_node
    
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next
       
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
      length = 0
      i = 0
      current_node = self.head
      while current_node != None:
        current_node = current_node.next
        length += 1
      current_node = self.head
      while i < length // 2:
        current_node = current_node.next
        i += 1
      return current_node.data
      

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(6)
list1.printList()
print(list1.printMiddle() )

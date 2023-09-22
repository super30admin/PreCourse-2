#time complexity: O(n)
#space complexity : O(1)
# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data): 
      self.value = data
      self.next = None
        
class LinkedList: 
    def __init__(self, data):    #Linkedlist constructor
      new_node = Node(data)
      self.head = new_node
      self.tail = new_node
      self.length = 1
      
    def push(self, new_data): #function to push items in linked list
      new_node = Node(data)
      if self.length == 0:
            self.head = new_node
            self.tail = new_node
      else:
            self.tail.next = new_node
            self.tail = new_node
      self.length += 1
      return True
        
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):      
      mid = int(self.length/2)      #taking index of middle node
      temp = self.head
      if self.length%2 == 0:        #if Linkedlist has even nodes then prints two middle numbers
            for i in range(mid-1):
                temp = temp.next
            print(f"Middle is: {temp.value} & {temp.next.value}")
      else:                         #if Linkedlist has odd nodes then prints one middle number
            for i in range(mid):
                temp=temp.next
            print(f"Middle is: {temp.value}")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

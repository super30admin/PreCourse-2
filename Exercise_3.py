# Node class  
#Time Complexity is nlogn
#Space complexity is in order of 0(1) for all operation of linkedlist
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
      self.data = data
      self.next = None
 
class LinkedList: 
  
    def __init__(self): 
      self.head = None
  
    def push(self, new_data):
      #adding the data in the linked list on the head if the head is null 
      if (self.head == None):
        self.head = Node(new_data)
        self.next = None
        return
      #data is added in the linked list at the tail 
      #with the help of the while loop the pointer will point on the last added data
      temp = self.head
      while temp.next:
          temp = temp.next
      #data is appended at the tail 
      temp.next = Node(new_data)
      temp.next.next= None
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
      temp = self.head
      count = 0
      #with the help of the while loop will count the total number of data in the linkedlist
      while temp.next:
        temp = temp.next
        count+=1
      temp = self.head
      mid = count//2
      count = 0
      #with the help of this while loop we will get the middle data
      #temp variable will be move equal number of steps from first data till count of mid variable
      while temp.next:
        if count == mid:
          return(temp.data)
        temp = temp.next
        count+=1
     


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()

"""
Time Complexity - 
push - O(n)
printMiddle - O(n/2)

Space Complexity - O(n)

"""

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self,data,next=None):
      self.data=data
      self.next=None
        
class LinkedList: 
  
  def __init__(self):
    self.headval=None
      
  def push(self, new_data):
    head=self.headval
    newnode=Node(new_data)
    if head==None:
      self.headval=newnode
    else:
      cur=head
      while cur.next:
        cur=cur.next
      cur.next=newnode
  
    # Function to get the middle of  
    # the linked list 
  def printMiddle(self):
    if self.headval.next:
      if self.headval.next.next:
        # creating two pointers
        # one will increment by 1 node
        # two will increment by 2 nodes everytime
        # hence by the time two reaches the end of linked list
        # one will be at the middle
        one=self.headval
        two=self.headval
        while two.next:
          if two.next.next:
            # pointing the next node to the next node
            two=two.next.next
            # pointing to the next node
          one=one.next
        print(one.data)
      

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle()
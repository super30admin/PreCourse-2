'''
Time and space complexity:
initialization: Time -> O(1); Space -> O(1)
push(): Time -> O(1); Space -> O(1)
printMiddle(): Time -> O(n); Space -> O(1)
'''

# Node class  
class Node:

  # Function to initialise the node object  
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList: 

  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, new_data):
    newNode = Node(new_data)
    newNode.next = self.head
    self.head = newNode
    self.size += 1

  # Function to get the middle of  
  # the linked list 
  def printMiddle(self):
    if not self.head:
      print('empty list!!!')
      return

    counter = self.size//2
    pointer = self.head

    while pointer:
      if counter == 0:
        print(pointer.data)
        return
      pointer = pointer.next
      counter -= 1
    return

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(12)
list1.push(86)
list1.push(9878)
list1.push(21)
list1.push(145)
list1.push(13)
list1.push(43)
list1.push(216)
list1.push(14)
list1.printMiddle() 

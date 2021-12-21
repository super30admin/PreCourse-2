# Node class  
#Exercise_3 : Find Mid Point of a Singly Linked List.

#O(n) to find length and push elements

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = Node(None)
  
    def push(self, new_data): 
        temp = self.head
        new_node = Node(new_data)
        while(temp.next):
            temp =temp.next
        temp.next = new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        length = 0
        runner = self.head
        while(runner):
            length += 1
            runner =runner.next
        mid = (length//2)-1
        temp_runner = self.head
        while(mid>=0):
            temp_runner = temp_runner.next
            mid -= 1
        return temp_runner.data

# 0 1 2 3 4 5 6 7 8 9

# Driver code 
list1 = LinkedList() 
# list1.push(5) 
# list1.push(4) 
# list1.push(2) 
# list1.push(3) 
# list1.push(1) 
for i in range(10):
    list1.push(i)
print(list1.printMiddle())

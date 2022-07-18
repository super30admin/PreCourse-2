# Node class  
# Time complexity - O(n)  Space Complexity - O(1)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self): 
        self.head = None
        self.tail = None
  
    def push(self, new_data): 
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    # Function to get the middle of  the linked list
    def printMiddle(self):
        dictu = {}
        dictu1 = {}
        temp = self.head
        count = 0
        while temp:
            dictu[count] = temp.data
            dictu1[count] = temp
            temp = temp.next
            count += 1
        print("middle element of linked list is " + str(dictu[count//2]))
        print("middle element is at the node ", end=" ")
        print(dictu1[count//2])

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()
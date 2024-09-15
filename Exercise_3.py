# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        self.length = 0
        self.last = None
  
    def push(self, new_data):
        node = Node(data=new_data)

        if self.head == None:
            self.head = node
            self.last = self.head
        else:
            self.last.next = node
            self.last = node
        # Another version where time complexity is O(N) for pushing
        '''temp = self.head
        if temp == None:
            self.head = node
        else:
            while temp.next!=None:
                temp = temp.next
            temp.next = node'''
        self.length+=1

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.length ==0:
            return -1
        else:
            mid  = int(self.length/2)
            if self.length%2 !=0:
                mid +=1
             #if there odd  length then add +1 to the mid location
            # if there are even length then returing the first location
            temp = self.head

            count = mid-1
            while count!=0:
                temp = temp.next
                count-=1
            return temp.data


# Driver code 
list1 = LinkedList() 
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
print(list1.printMiddle())

#Complexities

# time complexities push - O(1)
# time complexity middle - O(N)
# space complexity - O(N)

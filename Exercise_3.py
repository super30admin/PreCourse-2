
#time complexity:O(N)
#space complexity: O(k) where k is constant variable mid
#passed all cases on LeetCode: yes
#difficulty faced: trying to come with condition of while loop
# comments: traverse to the end and count the # of nodes, then 
           # traverse again till count/2, return the node for odd or 2 nodes for even count
           #decrementing the half count from count/2


# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None

    #pushing to the front of the LL:
    def push(self, new_data): 
        newnode = Node(new_data)

        newnode.next = self.head
        self.head = newnode

        return self.head
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next
        #print(count)    
        
        temp = self.head
        half_count = count//2

        while half_count != 0:
            temp = temp.next
            half_count -= 1
        print(temp.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
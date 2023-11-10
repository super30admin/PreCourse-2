# Time Complexity : O(N)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None 
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
  
    def push(self, new_data):
        #Created a newnode
        newnode = Node(new_data)
        #Checking if there is any node present or not in list and if not then assigning head to newnode
        if(self.head == None):
            self.head = newnode
        #If there are node present then assigning newnode after the last node
        else:
            node = self.head
            while(node.next != None):
                node = node.next
            node.next = newnode
  
    # Function to get the middle of  
    # the linked list 
    #Approach 1: Counting all node and then dividing count by 2 to find middle value
    def printMiddle(self):
        count = 0
        node = self.head
        while(node.next != None):
            node = node.next
            count += 1
        node = self.head
        i = 0
        while(i != count//2):
            node = node.next
            i += 1
        print(node.data)
    #Approach 2: Taking 2 node, first one traversing in increment of 1 and second one traversing in incremet of two so when
    #2nd node reaches last node at that time 1st node reaches the middle and then simply printing 1st node data 
    def printMiddle1(self):
        node = self.head
        node1 = self.head
        while(node1.next != None):
            node = node.next
            node1 = node1.next.next
        print(node.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle1() 

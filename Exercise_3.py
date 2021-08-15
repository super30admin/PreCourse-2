"""
Time Complexity- O(n)- for printing the middle element since for checking the size of the array we first traverse
n times and going till the middle element takes n/2 times so total time complexity is O(n + n/2)-O(n)
Space Complexity-we declare current node and size and each takes n iterations so im supposing the complexity will be o(n)
Explanation:We will find out the size of the linked list and then traverse the linked list till the middle point
Issue- Issue in matching this code on leetcode; have to figure it out, my python "object oriented " coding is not that good.
"""

# Node class
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self):
        self.head=Node(data=None)
        
  
    def push(self, new_data):
        newNode=Node(new_data)
        currentNode=self.head
        while currentNode.next!=None:
            currentNode=currentNode.next
        currentNode.next=newNode
        newNode.next=None


    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        size=0
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
            size+=1
        # print("The size is", size)
        # print("size by half is ", size//2)
        currentNode=self.head
        for i in range(size//2+1):
            currentNode=currentNode.next
            print("element", i, " is ", currentNode.data)
        print(currentNode.data)

    def printlist(self):
        currentNode=self.head
        while currentNode.next!=None:
            currentNode=currentNode.next
            print(currentNode.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printlist()
list1.printMiddle() 

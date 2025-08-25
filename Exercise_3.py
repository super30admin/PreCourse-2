# Time Complexity : O(len(LinkedList) / 2) = O(N / 2) - Taken for printMiddle() function
# Space Complexity : O(len(LinkedList)) = O(N) = Non-Contiguous space of O(N). Each node stores data and reference to the next node.
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach
# If length of LinkedList is Odd, then we have only one middle
# If length of LinkedList is Even, then we have two middle elements. Here I am returning the First Middle.
# Example if LinkedList is [1,2,3,4] then my first middle would be 2
# Here I am using fast and slow pointer approach. Our fast pointer travels at a speed of 2 times the speed of the slow pointer.
# So when my fast pointer has covered a distance of 2*x, our slow pointer reaches a distance of x. Using this analogy, when
# our fast pointer reaches the last node, our slow pointer has reached the middle of the LinkedList


# Node class  
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
        newNode = Node(new_data)
        if(not self.head):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if(not self.head):
            print("LinkedList is Empty")
            return
        
        slow = self.head
        fast = self.head

        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next

        print(slow.data)




# Driver code 
list1 = LinkedList()
list1.printMiddle()
list1.push(5)
list1.printMiddle() 
list1.push(4)
list1.printMiddle() 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()
list1.push(20)
list1.printMiddle()

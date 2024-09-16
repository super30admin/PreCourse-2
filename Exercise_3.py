# Time Complexity : push() - O(1), printMiddle() - O(n^2)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : I was not able to think of a solution where I can find the middle
  # with obtaining the length of the LinkedList, and thats why my solution is O(n^2)


# Your code here along with comments explaining your approach
'''
1. Pushing the node is simple, attaching the new node to head and , reinitializing head to be pointing to the newly added node
2. For finding the middle element, first I have cretaed a separate function calculates the length of the LL in O(n)
3. Then, it traverses the Linked list to the middle length(n)//2, and fetched the middle element
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
        
  
    def push(self, new_data):

        new_data_node = Node(new_data)
        if self.head is None:
            self.head = new_data_node

        else:
            new_data_node.next = self.head
            self.head = new_data_node
        

    def get_length(self):
        node_iterator = self.head

        count = 0
        while node_iterator:
            count += 1
            node_iterator = node_iterator.next

        return count

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 

        length = self.get_length()

        mid_element = int((length-1)//2)
        node_iterator = self.head
        c = 0
        while node_iterator and c < mid_element:
            node_iterator = node_iterator.next
            c = c + 1

        print (node_iterator.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(6)
list1.printMiddle() 

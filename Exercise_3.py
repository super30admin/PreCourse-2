# Node class  
class Node:  
   # Function to initialise the node object
    def __init__(self, data):
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self):
        self.head=None
        
  
    # def push(self, new_data):
    #     newnode=Node(new_data)
    #     newnode.next=self.head
    #     self.head=newnode

    def push(self, new_data):

        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next is not None):
            last = last.next


        last.next = new_node



        # Function to get the middle of
    # the linked list 
    def printMiddle(self):
        slowpointer=self.head
        fastpointer=self.head
        if self.head is not None:
            while(fastpointer is not None and fastpointer.next is not None):
                fastpointer=fastpointer.next.next
                slowpointer=slowpointer.next
            print( slowpointer.data)
# Driver code 
list1 = LinkedList() 
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
list1.push(6)
list1.push(7)
list1.push(8)
list1.push(9)
list1.printMiddle() 

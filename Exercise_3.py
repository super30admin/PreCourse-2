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
        self.length = 0
  
    def push(self, new_data):
        new_node = Node(new_data)
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.length +=1
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # use fast and slow pointer to get the middle of linked list
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(slow.data)

    def __str__(self) -> str:
        temp = self.head
        elements_in_list = []
        while temp:
            elements_in_list.append(temp.data)
            temp = temp.next
        return str(elements_in_list)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

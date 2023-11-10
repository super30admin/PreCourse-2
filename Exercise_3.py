# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None  
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
    
    def size(self):
        count = 0
        iter_node = self.head
        while(iter_node):
            iter_node = iter_node.next
            count += 1
        return count
      
    def push(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
        
        else:
            iter_node = self.head
            while (iter_node.next != None):
                iter_node = iter_node.next
            
            iter_node.next = Node(new_data)
            print()
        
    
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        import math
        linked_list_size = self.size()
        count = 0
        iter_node = self.head
        middle_element = None 
        while (iter_node):
            if count == math.ceil(linked_list_size / 2)-1:
                middle_element = iter_node.data
                break;
            iter_node = iter_node.next
            count += 1
        print(middle_element)
        return middle_element

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(41)
list1.push(88)


list1.size()
list1.printMiddle() 


# Time Complexity: O(1) for initialization, O(1) for push(), O(n) for print_LL(), O(n) for printMiddle()
# Space Complexity: O(n) for push() since a new node is added each time, O(1) for print_LL() and printMiddle()
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next  
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        pass

    def print_LL(self):
        curr = self.head
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
  
    def push(self, new_data):
        if self.head == None:
            new_node = Node(new_data)
            self.head = new_node
        else:
            new_node = Node(new_data)
            new_node.next = self.head        
            self.head = new_node
    def printMiddle(self):
        curr = self.head
        temp = self.head

        while curr and curr.next and temp and temp.next:
            curr = curr.next
            temp = temp.next.next

        print("\n Middle Element",curr.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.print_LL()
list1.printMiddle() 


#fast and slow pointers
#            next
#      cur 
# 5 --  4 --- 2 --- 3 --- 1
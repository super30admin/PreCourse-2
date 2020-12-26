# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data =None, next=None):
        self.data = data
        self.next = next
        
class LinkedList: 
    def __init__(self): 
        self.head = None 
    def push(self, new_data):
        newNode = Node(new_data)
        if not self.head:
            self.head = newNode
            return
        else:
            # traverse till end
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode     

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # We perform this using slow- fast pointers. Using this technique - the slow pointer always stops at middle
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Value of the middle node: ", slow.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
print(list1.head.data, list1.head.next.data, list1.head.next.next.data, list1.head.next.next.next.data, list1.head.next.next.next.next.data)
list1.printMiddle() 

# Input: 5 -> 4 -> 2 -> 3 -> 1
# Result: 2 -> 3 -> 1 (mid.data -> mid.next.data -> mid.next.next.data)

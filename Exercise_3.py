# Program name - Script to find the mid element single linked list
# Author - Prajakta Pardeshi

# Time complexity - O(n)

# Space complexity  O(1) 


# class node willl define the structure of the node
class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        node = ListNode(data)
 
        if self.head is None:
            self.head = node
            return

        # go to the last node
        end = self.head
        while (end.next):
            end = end.next
            
        end.next =  node
        return
        
    def findMiddle(self):
        """
        Find the mid element 
        """
      
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print("The middle element is ", slow.data)
        return False
    
     
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        
        if not self.head:
            return
        temp = self.head

        # Check if head node is to be deleted
        if self.head.data == key:
            self.head = temp.next
            print("Deleted node is " + str(self.head.data))
            return

        while(temp.next):
            if temp.next.data == key:
                print("Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        print ("Node not found")
        return
    
    # Print the linked list
    def display(self):
        if self.head == None:
            print("List is empty")

        node = self.head 
        while(node):
            print(node.data, end="  ")
            node = node.next
        print("\n")
        
        
sl = SinglyLinkedList()
sl.append(1)
sl.append(2)
sl.append(3)
sl.append(4)
sl.append(5)
sl.display()
sl.findMiddle()
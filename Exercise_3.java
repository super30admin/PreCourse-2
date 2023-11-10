class LinkedList 
{ 
    Node head; // head of linked list 
  
    /* Linked list node */
    class Node 
    { 
        int data; 
        Node next; 
        Node(int d) 
        { 
            data = d; 
            next = null; 
        } 
    } 
  
        /**
    ## problem - find a mid point and print the middle in a singly linkedlist.
    ## Assumptions 
    - list is not empty.
    ## possible solutions
    - 1 2 3 4 5 odd mid point is 3.
    - 1 2 3 4    even the mid is 2.
    - slowptr - head
    - fastptr - head
    - Traverse slowptr 1 step and fastptr 2 steps, When fastptr.next is null then at that point the value of slowptr is 
    the middle element of the list.
    Time Complexity - O(n) where n is the number of nodes in the linkedlist
    Space Complexity - O(n) 
    
    TestCases 
     - even list
     - odd list
     - empty list
     - list with single element
     - list with 2 elements
    **/
    /* Function to print middle of linked list */
    void printMiddle() 
    { 
       if (head == null)
       {
           System.out.pritnln("LinkedList is empty");
           return;
       }
       
       Node slowPtr = head;
       Node fastPtr = head;
        
        while(slowPtr != null && fastPtr != null && fastPtr.next != null)
        {
            slowPtr = slowPtr.next;
            fastPtr = fastPtr.next.next;
        }
        
        System.out.println(" Middle element of the list is :"+slowPtr.data);
    } 
  
    public void push(int new_data) 
    { 
        Node new_node = new Node(new_data); 
        new_node.next = head; 
        head = new_node; 
    } 

    public void printList() 
    { 
        Node tnode = head; 
        while (tnode != null) 
        { 
            System.out.print(tnode.data+"->"); 
            tnode = tnode.next; 
        } 
        System.out.println("NULL"); 
    } 
  
    public static void main(String [] args) 
    { 
        LinkedList llist = new LinkedList(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle(); 
        } 
    } 
} 
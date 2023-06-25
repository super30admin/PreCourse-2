
// Time Complexity: O(n)
// Space Complexity: O(1)

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
  
    /* Function to print middle of linked list */
   //Complete this function
    void printMiddle() 
    { 
        //Write your code here
	//Implement using Fast and slow pointers

        if(head == null)
        {
            System.out.println("Linked List is Empty");
            return;
        }


        Node slowPtr = head; // Slow Pointer moves one node at a time
        Node fastPtr = head; // Fast Pointer moves two nodes at a time

        while(fastPtr != null && fastPtr.next != null)
        {
            fastPtr = fastPtr.next.next; // Move fast pointer two nodes at a time
            slowPtr = slowPtr.next; // Move slow pointer one node at a time
        }

        System.out.println("Middle of Linked List: " + slowPtr.data);

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
// Time Complexity : O(n) as we are traversing till the end of the list once
// Space Complexity : O(1) as we are always going to need just 2 pointers regardless of the size of the list and no additional data structure is needed.
// Did this code successfully run on Leetcode : N/A
//Assumption: if it is an even-numbered list n, the method will return the ceil(n/2)th element in the list
//for example: if the list is 1->2->3->4, the middle will be 3
// Any problem you faced while coding this :
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
        if(head == null)
        {
            System.out.println("The list is empty");
            return;
        }

        //initially both point to the head
        Node slowPointer = head;
        Node fastPointer = head;

        if(head.next == null)
        {
            System.out.println("The middle element is: " + head.data);
            return;
        }

        //let the fast pointer traverse to the end of the list
        while(fastPointer != null && fastPointer.next != null)
        {
            fastPointer = fastPointer.next.next;
            slowPointer = slowPointer.next;
        }

        System.out.println("The middle element is: " + slowPointer.data);

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
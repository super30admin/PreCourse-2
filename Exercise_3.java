// Time Complexity : fast pointer is traversing through whole linked list causing an O(n) complexity
// Space Complexity : Only an additional pointers to head are created, so space complexity: O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Got confused with print statement in for loop

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
        // In some scenarios if the head would be null we can just return head
        if(head==null) {
            System.out.println(head.data);
        }
        // we take 2 pointers, slow and fast which would run at different paces
        Node trav1 = head;
        Node trav2 = head;
        // if fast pointer is not null and its next is also not null run fast pointer 2 steps and slow pointer 1 step.
        // So while the first pointer reach the last position, slow pointer will reach only at mid.
        // we can print slow pointer a it is mid value
        while(trav1!=null && trav1.next!=null) {
            trav1 = trav1.next.next;
            trav2 = trav2.next;
        }
        System.out.println(trav2.data);
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
        } 

        // these function call inside for are causing a lot of confusion
        llist.printList(); 
        llist.printMiddle(); 
    } 
} 
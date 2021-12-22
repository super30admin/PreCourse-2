// Time Complexity : O (n)
// Space Complexity : O (1)
// Did this code successfully run on Leetcode : Ran it on VS Code. 
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
// Create two node pointers slow and fast and assign value as head to both the node pointers. Use while loop
// to check if fast and the next node to fast is not null. If we get the fast node as null it means that there is
// even number of nodes and there are two mid points which are the slow node pointer and the node previous to slow
// Keep track of the node before the slow node in every iteration using temp variable. If the node next to fast is
// null it means that there are odd number of nodes and midpoint is given by slow pointer node. 

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
        Node slow = new Node(head.data); 
        Node fast = new Node(head.data);
        slow = head;
        fast = head; 
        int temp = 0;

        while(fast != null && fast.next != null){
            temp = slow.data;
            slow = slow.next;
            fast = fast.next.next;
        }
        if(fast == null){
            System.out.println(temp+" "+slow.data);
        }
        else{
            System.out.println(slow.data);
        }
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
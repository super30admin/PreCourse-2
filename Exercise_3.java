// Time Complexity : O(n)
// Space Complexity : O(n)  n-number of nodes.
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : -


// Your code here along with comments explaining your approach
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
		Node fast=head;
		Node slow=head;
	
	while(fast!=null && fast.next!=null)
	{
		fast=fast.next.next; // increments by 2 so that when it reaches the end slow will be in the middle
		slow=slow.next;
		
	}
	System.out.println("Middle "+slow.data);
	
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
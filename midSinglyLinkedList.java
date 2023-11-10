//Precourse 2: Exercise 3   --  Find mid point of Singly Linked List
// Time Complexity : O(n) because fast pointer navigates through all nodes from head till tail
// Space Complexity : O(n) for storing n elements also as this sorting technique is in place.
// Any problem you faced while coding this : no

/*Output:
 * 5->NULL
The middle of Linked List is5
4->5->NULL
The middle of Linked List is5
3->4->5->NULL
The middle of Linked List is4
2->3->4->5->NULL
The middle of Linked List is4
1->2->3->4->5->NULL
The middle of Linked List is3
 */
public class midSinglyLinkedList { 
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
	        //Write your code here and implement using Fast and slow pointers
	    	Node slow=head;
	    	Node fast=head;
	    	while(fast!=null && fast.next != null)
	    	{
	    		fast=fast.next.next;
	    		slow=slow.next;
	    	}
	    	System.out.println("The middle of Linked List is" + slow.data);
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
	    	midSinglyLinkedList llist = new midSinglyLinkedList(); 
	        for (int i=5; i>0; --i) 
	        { 
	            llist.push(i); 
	            llist.printList(); 
	            llist.printMiddle(); 
	        } 
	    } 
	
}

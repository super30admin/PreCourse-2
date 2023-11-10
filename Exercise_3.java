package Ex3;

//Time Complexity : O(n)
//Space Complexity : O(1)
//Did this code successfully run on Leetcode :
//Any problem you faced while coding this :

public class LinkedList {

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
	    	
	    	Node temp1 = head;
	    	Node temp2 = head;
	    	
	    	if(head!=null)
	    	{
	    		while(temp2!=null && temp2.next!=null )
	    		{
	    			temp1= temp1.next;
	    			temp2 = temp2.next.next;
	    		}
	    		
	    		System.out.println("Middle element of the list is " + temp1.data);
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


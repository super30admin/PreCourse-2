/**
 *	Time Complexity : O(n)
 *
 * 1. initialize midIndex to starting index
 * 2. when index is odd move midIndex by one
 * 3. print the midIndex item from the LinkedList
 */

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
    	int midIndex = 0;
        Node midElement = head;
        
        Node headTemp = head;
        
     
        while (headTemp != null)
        {
            if ((midIndex % 2) == 1)
            	midElement = midElement.next;
     
            ++midIndex;
            headTemp = headTemp.next;
        }
     
        if (midElement != null)
            System.out.println("middle element="+midElement.data);
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
  
} 
public class Exercise_3{
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
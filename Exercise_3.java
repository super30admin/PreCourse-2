package precourse2;

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
    	Node slowPtr = head;
    	Node fastPtr = head;
    	if (head.next == null || head.next.next == null) {
    		System.out.println("Mid element "+ head.data);
    	}
    	else {
        	while(fastPtr.next!=null && fastPtr.next.next!=null) {
        		fastPtr = fastPtr.next.next;
        		slowPtr = slowPtr.next;
        	}
        	System.out.println("Mid element "+ slowPtr.data);
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
        for (int i=10; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle(); 
        } 
    } 

}

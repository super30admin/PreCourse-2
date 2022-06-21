//Time Complexity: O(n)
//Space Complexity: O(n)

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
  
    void printMiddle() 
    { 
		Node fp = head;
		Node sp = head;
		
		while(fp != null && fp.next!= null) {
			fp= fp.next.next;
			
			sp = sp.next;
		}
		
		System.out.println(sp.data);
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

class Driver{
	    public static void main(String [] args) 
	    { 
	        LinkedList llist = new LinkedList(); 
	        for (int i=15; i>0; --i) 
	        { 
	            llist.push(i); 

	        } 
            llist.printList(); 
            llist.printMiddle(); 
	    } 
} 
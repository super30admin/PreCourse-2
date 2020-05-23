// Time Complexity : o(n)
// Space Complexity : o(1)
// Did this code successfully run on Leetcode :
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
        //Write your code here
	//Implement using Fast and slow pointers
    	if(this.head == null) 
    		return;
    	
    	if(this.head.next == null) {
    		System.out.println(this.head.data);
    		return;
    	}
    	
    	Node s = this.head;
    	Node f = this.head;
    	
    	while(f!=null && f.next!=null) {
    		f = f.next.next;
    		s = s.next;
    	}
    	
    	System.out.println("middle node is: " + s.data);
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
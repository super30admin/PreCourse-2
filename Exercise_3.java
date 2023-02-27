//Time Complexity:O(n)
//Space Complexity:O(1)
// code executed successfully

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
     //iterate till mid node
    	if(head!=null) {
    		int mid = getLength()/2;
    		Node curr= head;
    		for(int i =1; i<=mid;i++) {
    			curr= curr.next;
    		}
    		System.out.println("middle element " + curr.data);
    		
    	}
   
    	    	
    } 
    //find length of linkedlist
   int getLength() {
	   int len =0;
	   Node curr= head;
	   while(curr!= null) {
		   
		   len++;
		   curr= curr.next;
		
	   }
	   return len;
	   
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
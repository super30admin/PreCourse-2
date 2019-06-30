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
    	//approach is: fast pointer traverses the list two nodes at a time while slow pointer traverses the list one node at a time
    	//once the fast pointer reaches the last node, the slow pointer has only reached upto the middle of the list
    	
    	Node f_ptr = head;
    	Node s_ptr = head;
    	
    	if(head!=null)//making sure the list is not empty
    	{
    		while(f_ptr!=null && f_ptr.next!=null)
    		{
    			f_ptr = f_ptr.next.next;
    			s_ptr = s_ptr.next;
    		}
    		System.out.println("Middle element of the linked list is: " +s_ptr.data);
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
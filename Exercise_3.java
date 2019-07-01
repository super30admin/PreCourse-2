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
        // brute force approach
	    // find total number of node and then find the middle by count/2.
	    int count= 0;

    	Node tnode = head;
        while (tnode != null)
        {
        	++count;
            tnode = tnode.next;

        }
        int middle = count/2;
        count =0;
        tnode = head;
        while (tnode != null &&  count<middle)
        {
        	++count;
            tnode = tnode.next;

        }
        System.out.println("The middle element with Brute Force is : [" +
                                tnode.data + "] \n");

        //Having  two pointer way
        Node slow = head;
        Node fast = head;
        if (head != null)
        {
            while (fast != null && fast.next != null)  // we have this checks, becuase ,if we traverse
            {
            	fast = fast.next.next;  //used next.next here to jump twice in the linked list.
                slow = slow.next;  //Moving the slow element one by one
                /// here idea is that when we traverse , ask a another variable traverse faster and when
                // the other variable reacher end , the main varible will be at middle, since other variable is taking two steps.
            }
            System.out.println("The middle element is [" +
                                slow.data + "] \n");
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

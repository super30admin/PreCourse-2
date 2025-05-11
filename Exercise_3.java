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
	Node slow = head;
	Node fast = head;
	//both conditions are crucial to avoid null pointer
	//if we have reached the next of end of the list then fast.next will lead to exception
	while(fast!=null && fast.next!=null)
	{
	    //going one step ahead
	    slow = slow.next;
	    //going two step ahead
	    fast = fast.next.next;
	}
	//we have reached the end of list with fast so slow must be at mid since it moves 1 for 2 steps of fast
	System.out.println(slow.data); 
	//it printed the second mid element in case of even length 
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

class LinkedListPC2 
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
    	// slow jumps by one while fast jumps by two so when the fast reaches the end the slow would be at the middle of the list
    	Node fast = head; 
    	Node slow = head;
    	while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
    	// Printing the middle element
    	System.out.println(slow.data);
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
        LinkedListPC2 llist = new LinkedListPC2(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            System.out.println("Middle: "); 
            llist.printMiddle();
        } 
    } 
} 
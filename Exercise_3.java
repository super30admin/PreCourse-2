class LinkedList 
{ 
    Node head; // head of linked list 
  
	//time- O(N)- where N are the number of nodes
	//space- O(1)
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
    
    ListNode fast= head;
        
    while(fast.next!= null && fast.next.next!=null){
        fast= fast.next.next;
        head= head.next;
    }
    //System.out.println(fast.val);
    
    if(fast.next!=null){
        head= head.next;
    }
    
    ListNode value=head;
    while(value!=null){
         System.out.println(value.val);
        value=value.next;
        
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

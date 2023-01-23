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
        //initializing slow and fast to head
        Node slow = head;
        Node fast = head;
        
        //checking fast isn't null, so is it's nect node
        while(fast != null && fast.next != null){
            slow = slow.next; //moving slow by 1 step
            fast = fast.next.next; //movong fast by 2 steps
        }

        //when fast reaches to the end of the ll, slow will reach the middle that time
        //hence we print the data at slow
        System.out.println("Mid element:" + slow.data);
      
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
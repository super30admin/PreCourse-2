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
    //Start both the pointers from the head
        Node slow = head; 
        Node fast = head; 
        if (head != null) 
        { 
            //Traverse the fast and slow pointer till fast pointer reaches null 
            while (fast != null && fast.next != null) 
            { 
                //if fast pointer hops 2 then slow pointer hops 1
                fast = fast.next.next; 
                slow = slow.next; 
            } 
            //When the fast pointer reaches null the slow pointer reaches at middle
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
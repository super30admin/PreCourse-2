package com.sthirty.precoursetwo.prblmthree;

class Exercise_3 
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
    	int count = 0;
        Node mid = head;
        Node temp=head;
        while (temp != null)
        {
     
            // Update mid, when 'count' 
            // is odd number 
            if ((count % 2) == 1)
                mid = mid.next;
     
            ++count;
            temp = temp.next;
        }
     
        // If empty list is provided 
        if (mid != null)
            System.out.println(mid.data);
    
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
        Exercise_3 llist = new Exercise_3(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle(); 
        } 
    } 
} 
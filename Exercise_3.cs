// Time Complexity :O(logN) where N = number of elements in list
// Space Complexity : O(1) 
using System;

class LinkedList 
{ 
    Node head; // head of linked list 
  
    /* Linked list node */
    class Node 
    { 
        public int data; 
        public Node next; 
        public Node(int d) 
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
        // Implement using Fast and slow pointers
        Node slowPointer = head;
        Node fastPointer = head;
        while (fastPointer.next !=null && fastPointer.next.next != null) 
        {
            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next.next;
        }
        Console.WriteLine("Middle of linked list is " + slowPointer.data);	
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
            Console.WriteLine(tnode.data+"->"); 
            tnode = tnode.next; 
        }
        Console.WriteLine("NULL"); 
    } 
  
    public static void Main(string[] args) 
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
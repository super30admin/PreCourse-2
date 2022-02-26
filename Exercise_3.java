/*
Time Complexity : O(N)
Space Complexity : O(1)
Did this code successfully run on Leetcode : yes
Any problem you faced while coding this : No
*/
class LinkedList 
{ 
    Node head; 

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

    void printMiddle() 
    {  Node slowPt = head;
        Node fastPt = head;

        while(fastPt  != null && fastPt.next != null){
            slowPt = slowPt.next;
            fastPt = fastPt.next.next;
        }
        System.out.println("Middle element is : " + slowPt.data);
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
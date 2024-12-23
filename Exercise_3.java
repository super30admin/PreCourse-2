// Time Complexity : O(n) -> I think it should be o(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : I faced issue while finding out the end condition when the loop should stop

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
        Node slow=head;        //Two pointers one slow and one fast
        Node fast=head;

        
        while(fast!=null && fast.next!=null){   //Condition till when the loop should iterate considering both even and odd number of nodes
            fast=fast.next.next;                //The fast pointer will move twice than slow pointer
            slow=slow.next;
        }
        System.out.println("Middle node is "+slow.data);
        

        //Write your code here
	//Implement using Fast and slow pointers

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
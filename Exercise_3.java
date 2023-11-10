/*
 Time Complexity->O(n) where n is size of linked list
 Space Complexity->O(1) //no extra space is needed
 */
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
        //slow pointer will move forward by one position
        Node slow=head;
        //fast pointer will move forward by two positions
        Node fast=head;
        //when list is of even or odd size,odd->fast.next==null,even->fast=null
        while(fast!=null && fast.next!=null)
        {
            slow=slow.next;
            fast=fast.next.next;
        }
        //fast pointer will reach to end and slow pointer will reach the middle
        System.out.println("Middle Element is "+slow.data);
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
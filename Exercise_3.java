// Time Complexity : O(N), iterate over the linked list
// Space Complexity : O(1), slow and fast pointer
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : no
/*
Finding middle of the linked list using slow and fast pointer, the slow pointer moves one by one element,
whereas the fast pointer moves twice of that, so as the fast pointer reaches to the end of the linked list
slow pointer reaches to the middle of the linked list and we can print the middle value
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
        //Write your code here
	//Implement using Fast and slow pointers
        Node slow = head;
        Node fast = head;

        while(fast!= null && fast.next!= null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        System.out.println("Middle linked list: "+ slow.data);
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
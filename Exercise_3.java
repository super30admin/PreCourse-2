//Time Complexity : O(n), as fast pointer would need to traverse the complete list
//Space Complexity : Space is constant in terms of printing the middle, however the space complexity of linkedlist would be O(n)
//Did this code successfully run on Leetcode :
//Any problem you faced while coding this : no


//Your code here along with comments explaining your approach


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
    	
    	Node fast = head;
    	Node slow = head;
    	// Moving fast pointer two times, and slow pointer 1 time, when fast reaches null, the slow would point to the middle element
    	while(fast!=null && fast.next!=null) {
    		fast = fast.next.next;
    		slow = slow.next;
    		
    	}
    	
    	System.out.println("Middle is : " + slow.data);
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
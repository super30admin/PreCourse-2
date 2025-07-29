//Time Complexity :O(n)
//Space Complexity :O(n)
//Did this code successfully run on Leetcode : yes
//Any problem you faced while coding this : had no idea about fast pointer, learnt
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
       if(head == null) {
			System.out.println("Empty list \n");
			return;
		}
		// Implement using Fast and slow pointers
		Node slowPointer = head;
		Node fastPointer = head;
		
		if(fastPointer.next == null || fastPointer.next.next == null ) {
			System.out.println("Less than 3 elements in the list \n");      // Edge case scenario
			return;
			
		}
		
		while(fastPointer != null && fastPointer.next != null ) {
			slowPointer = slowPointer.next;
			fastPointer = fastPointer.next.next;
		}
		System.out.println("Middle Element : " +  slowPointer.data + "\n");s
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

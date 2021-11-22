
/*
 * * Time Complexity: O(n)
 * 
 * Space Complexity: O(1)
 * 
 * This code ran successfully on Leetcode
 * 
 * Any problems you face while coding this - No
 * 
 * Approach: 
 * 1. Use two pointer one which will run fast and one that will run slow
 * 2. Fast pointer will move 2 nodes ahead in each run where as slow will go only one node ahead
 * 3. so for upto current no of nodes where fast pointer is, slow one gives the mid point
 * 4. so we keep fast pointer going ahead till fast.next.next != null and we put a condition 
 * 	  where fast or fast.next == null then we go out of loop
 * 5. once we out of loop we check if fast pointer can still go ahead as it is going 2 positions ahead in one go
 * 6. once fast pointer cannot go ahead, we have slow pointer actually pointing at mid node of linked list
 * 7. at the begining we put a check where we check if head is null or head.next is null
 *
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
    	
    	 if(head.next == null || head == null) {
    		 System.out.println(head.data);
    	 }
    	 else {
    		 Node fast = this.head;
             Node slow = this.head;
             
             
             while(fast.next.next != null){
                 fast = fast.next.next;
                 slow = slow.next;
                 if(fast.next == null || fast == null)break;
             }
             
             while(fast.next != null){
                 fast = fast.next;
                 slow = slow.next;     
                
             }
             
             System.out.println(slow.data); 
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

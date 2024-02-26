class LinkedList {
    // Time Complexity : O(n) as we need to traverse all elements in linkedlist
    // Space Complexity : O(1), no extra space needed other than constaants
    // Did this code successfully run on Leetcode : IDK
    // Any problem you faced while coding this :
    Node head; // head of linked list 
  
    /* Linked list node */
    class Node {
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
        if(head == null){
            System.out.println("EMPTY LinkedList");
        }

        // let the pointers race begin
        Node slow = head;
        Node fast = head;
        while(fast != null && fast.next != null) {
            slow = slow.next; // 1x speed
            fast = fast.next.next; //2x speed
        }

//        when fast reaches at the end, then slow will reach at the middle.
//        As fast is running at 2x speed (calling next twice) compared to slow
        System.out.println("Middle of LinkedList: " + slow.data);

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
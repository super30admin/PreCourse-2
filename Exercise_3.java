class LinkedList 
{ 
    Node head; // head of linked list 
  
    /*
      Time Complexity: O(n)

      Space Complexity: O(1)

      Did this code successfully run on Leetcode : Yes
      Any problem you faced while coding this : No
    */
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
      Node slow = head, fast = head;

      // 1 -> 2 -> 3 -> 4 -> 5

      while(fast.next != null){
        fast = fast.next;

        if(fast.next == null){
          System.out.println(slow.next.data);
          return;
        }

        slow = slow.next;
        fast = fast.next;
      }

      System.out.println(slow.data);
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
// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

/*
Approach:
I used slow and fast pointers to find the middle node.
Both pointers start from the head of the linked list.

1. First, check if the head is null.
   If it is, print that the linked list is empty and return.

2. Otherwise, run a while loop:
   It continues while fast is not null and fast.next is not null.

3. Inside the loop:
   Move the fast pointer two steps forward.
   Move the slow pointer one step forward.

4. When the loop ends, the slow pointer will be at the middle node.
   Print the value at the slow pointer.
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
        if(head == null) 
        {
            System.out.println("LinkedList is empty");
        }
        Node fast = head;
        Node slow = head;
        
        while(fast!=null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        System.out.println("The middle of LinkedList is: "+ slow.data);
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
// Time Complexity : O(n)
// Space Complexity : O(n)
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

        Node slow_ptr = head;
        Node fast_ptr = head;
        while(fast_ptr !=null && fast_ptr.next != null){
            fast_ptr = fast_ptr.next.next;
            slow_ptr = slow_ptr.next;
        }
        System.out.println("Middle Element ->" +slow_ptr.data);

    }
  
    public void push(int new_data) 
    { 

        Node newNode = new Node(new_data);
        newNode.next = head;
        head = newNode;





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
            //llist.push(null);
            llist.printList(); 
            llist.printMiddle();
        } 
    } 
} 
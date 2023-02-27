public class LinkedList
{
    /*
    Time Complexity : O(N) where N is size of Linked List
    Space Complexity : O(1)
    */
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
        int i=0;
        Node node = head;
        while(node !=null){
            node = node.next;
            i++;
        }
        int mid = i/2;
        int j=0;
        Node node1 = head;
        if(node1 !=null) {
            while (j < mid && node1 != null) {
                node1 = node1.next;
                j++;
            }
            System.out.println("Middle of linkedList " + node1.data);
        }
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
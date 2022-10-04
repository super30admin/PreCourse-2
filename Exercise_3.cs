// Time Complexity : O(n), where n is the size of the linked list
// Space Complexity : O(1)
class LinkedList 
{ 
    Node head; // head of linked list 
  
    /* Linked list node */
    class Node 
    { 
        public int Data; 
        public Node Next; 
        public Node(int d) 
        { 
            Data = d; 
            Next = null; 
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

        while(fast!=null && fast.Next!=null){
            slow = slow.Next;
            fast = fast.Next.Next;
        }
        Console.WriteLine(slow.Data + " is the middle element.");
    } 
  
    public void push(int new_data) 
    { 
        Node new_node = new Node(new_data); 
        new_node.Next = head; 
        head = new_node; 
    } 

    public void printList() 
    { 
        Node tnode = head; 
        while (tnode != null) 
        { 
            Console.Write(tnode.Data+"->"); 
            tnode = tnode.Next; 
        } 
        Console.WriteLine("NULL"); 
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
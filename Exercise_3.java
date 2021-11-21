//Time Complexity:O(n/2) as we iterate with the help of fastPointer visiting every alternate node.
//Space Complexity: Constant as we are using just 2 pointers.

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
        Node fastPointer = head;
        Node slowPointer = head;
        while(fastPointer != null || fastPointer.next != null){
            //we define 2 pointers, for every 2 steps taken by the fastPointer, the slow pointer makes a move. Hece by the time fastPointer is either null or the next to it is null,
            //the slowPointer would point to the middle of the list
            fastPointer = fastPointer.next.next;
            slowPointer = slowPointer.next;
        }
        System.out.println(slowPointer.data);
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

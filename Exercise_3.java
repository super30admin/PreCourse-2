public class LinkedList {
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

        /* Time Complexity: Here we are moving fast pointer 2 steps at a time,
                            loop runs for n/2 times. So, O(n/2) which is asymptotically equal to O(n).

           Space Complexity: We are just moving pointers over list no extra space is consumed. O(1)

        */


        if(head != null) {
            Node slowPtr = head;
            Node fastPtr = head;
            while (fastPtr != null && fastPtr.next != null) {
                slowPtr = slowPtr.next;
                if (fastPtr.next.next != null)
                    fastPtr = fastPtr.next.next;
                else
                    fastPtr = fastPtr.next;
            }
            System.out.println("Middle Element is: " + slowPtr.data);
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

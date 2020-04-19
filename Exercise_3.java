class LinkedList
{
    Node head;

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



    /**
     * Function to print middle of linked list
     */
    //Time complexity is:o(n)(it is n/2 but we skip constant and it becomes o(n))
    //space complexity is:0(1) as we are just using 2 pointers so it is always going to be constant irrespective of the list length
    void printMiddle()
    {
        Node slow=head;
        Node fast=head;
        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        System.out.println(slow.data);

    }

    /**
     * add the node at the head of linedlist
     * @param new_data new node data to be added in list
     */
    //Time complexity is: o(1)
    //Space complexity is:o(1)
    public void push(int new_data)
    {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }
/**
 * Print the data of linkedlist
 */
//Time complexity is:o(n)
//Spce complexity is:o(1)
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
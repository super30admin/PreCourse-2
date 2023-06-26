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
        Node fast = head;
        Node slow = head;

        while(fast !=null && fast.next!=null){
            fast=fast.next.next;
            slow=slow.next;
        }
        System.out.print("Middle Element of linkedList is " + slow.data);

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

    //Time Complexity is O(N)
    //Space Complexity is O(1)

    public static void main(String [] args)
    {
        LinkedList llist = new LinkedList();
        for (int i=4; i>0; --i)
        {
            llist.push(i);
            llist.printList();
        }
        llist.printMiddle();
    }
}




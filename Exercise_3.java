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
        int i = 0;
        int j = 0;
        Node temp = head;
        Node temp2 = head;
        Node temp3 = head;
        while(temp.next!=null){
            i++;
            temp = temp.next;
        }
        while(temp2!=null && temp2.next!=null){
            j++;
            temp2 = temp2.next.next;
        }
        for (int x = 0;x<=i-j;x++){
            if(x == i-j){
                System.out.println(temp3.data);
            }
            temp3 = temp3.next;
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
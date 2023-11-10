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
        if(head!=null){
//            System.out.printf("head = "+head.data);
            Node slow=head;
            Node fast;
            if(head.next!=null){
                 fast=head.next;
            }else{
                System.out.println("middle element " + head.data);
            return;
            }
            while(fast.next!=null ){
                if(fast.next.next!=null){
                    fast=fast.next.next;
                    slow=slow.next;
                }else{
                    slow=slow.next;
                    fast=fast.next;
                }

            }
            System.out.println("middle element  "+slow.data);
        }else{
            System.out.printf("Given list is not initialized.");
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
        System.out.print("Current Array = ");
        while (tnode != null)
        {

            System.out.print( tnode.data+"->");
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
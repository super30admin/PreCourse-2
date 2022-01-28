// O(N) time and o(1) space as the list is already created
// slow moves 1 , fast moves 2 when fast is at end of list, slow will be in middle
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
        if(head == null) return;
        if(head.next == null || head.next.next == null) {
          System.out.println(head.data);
          return;
        }
//1, 2,3
        Node slow = head;
        Node fast = head.next.next;

        while(fast != null ){
          slow = slow.next;
          if(fast.next != null){
            fast = fast.next.next;
          }
          else{
            fast = null;
          }
        }
       System.out.println(slow.data);
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

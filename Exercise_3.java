// Time Complexity : O(N/2) which is same as O(N)
// Space Complexity : O(1) since we are only using pointers and no extra space
// Did this code successfully run on Leetcode : Ran it locally on IDE and works
                          //with multiple test cases
// Any problem you faced while coding this : No

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
        /*
          we start with two pointers slow and fast, when slow advances one step,
          fast does two steps at a time and as soon as fast finishes traversing,
          the slow might have reached the middle.
        */
        Node slow = this.head;
        Node fast = this.head;

        while(fast ! = null)
        {
          if(fast.next != null)
          {
            fast = fast.next.next;
          }
          else
          {
            System.out.println(slow.data);
            return;
          }
          slow = slow.next;
        }

        System.out.println(slow.data);
        return;

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

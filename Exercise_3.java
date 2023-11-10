// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Tested successfully on local code editor.
// Any problem you faced while coding this : No

//Approach:I have kept two pointers, fast and slow, both of which point to the head at the beginning. Fast ptr is incremented twice while the slow ptr is incremented only once.
//The result is when the fast ptr will be at the end of the list the slow ptr will be at the middle of the list. then I have returned the data at the middle node.

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
        while(fast != null && slow != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
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
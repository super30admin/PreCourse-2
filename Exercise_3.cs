public class LinkedList
{
    // Time Complexity : O(N)- since we are using 2 pointers to traverse the linked list
    // Space Complexity : O(1)
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : No
    public Node head; // head of linked list 

    /* Linked list node */
    public class Node
    {
        public int data;
        public Node next;
        public Node(int d)
        {
            data = d;
            next = null;
        }
    }

    /* Function to print middle of linked list */
    //Complete this function
    public void printMiddle()
    {
        //Write your code here
        //Implement using Fast and slow pointers
        Node slow = head;
        Node fast = head;
        while (fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        Console.WriteLine("Middle node is: " + slow.data);
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
            Console.WriteLine(tnode.data + "->");
            tnode = tnode.next;
        }
        Console.WriteLine("NULL");
    }
}

// Driver method to test above 
public static void Main(String[] args)
{
    MiddleLinkedList llist = new MiddleLinkedList();
    for (int i = 16; i > 0; --i)
    {
        llist.push(i);
        llist.printList();
        llist.printMiddle();
    }
}

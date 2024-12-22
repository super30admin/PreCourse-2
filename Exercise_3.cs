class LinkedList
{
    Node head; // head of linked list 

    /* Linked list node */
    class Node
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
    public void PrintMiddle()
    {
        if (head == null)
        {
            Console.WriteLine("Empty LinkedList");
        }
        if (head.next == null || head.next.next == null)
        {
            Console.WriteLine($"Middle Element is {head.data}");
        }
        var slow = head;
        var fast = head;
        //Write your code here
        //Implement using Fast and slow pointers
        while (fast.next != null && fast.next.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        Console.WriteLine($"Middle Element is {slow.data}");
    }

    public void Push(int new_data)
    {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }

    public void PrintList()
    {
        Node tnode = head;
        while (tnode != null)
        {
            Console.WriteLine(tnode.data + "->");
            tnode = tnode.next;
        }
        Console.WriteLine("NULL");
    }

    static void Main(string[] args)
    {
        LinkedList linkedList = new LinkedList();
        for (int i = 15; i > 0; --i)
        {
            linkedList.Push(i);
            linkedList.PrintList();
            linkedList.PrintMiddle();
        }
    }
}
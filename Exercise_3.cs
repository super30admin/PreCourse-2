
using System;
/*
Space complexity - O(1)
Time complexity - O(n)

OUTPUT -
15->NULLMiddle node data : 15
14->15->NULLMiddle node data : 15
13->14->15->NULLMiddle node data : 14
12->13->14->15->NULLMiddle node data : 14
11->12->13->14->15->NULLMiddle node data : 13
10->11->12->13->14->15->NULLMiddle node data : 13
9->10->11->12->13->14->15->NULLMiddle node data : 12
8->9->10->11->12->13->14->15->NULLMiddle node data : 12
7->8->9->10->11->12->13->14->15->NULLMiddle node data : 11
6->7->8->9->10->11->12->13->14->15->NULLMiddle node data : 11
5->6->7->8->9->10->11->12->13->14->15->NULLMiddle node data : 10
4->5->6->7->8->9->10->11->12->13->14->15->NULLMiddle node data : 10
3->4->5->6->7->8->9->10->11->12->13->14->15->NULLMiddle node data : 9
2->3->4->5->6->7->8->9->10->11->12->13->14->15->NULLMiddle node data : 9
1->2->3->4->5->6->7->8->9->10->11->12->13->14->15->NULLMiddle node data : 8

Approach - Fast pointer travels at twice the speed as slow pointer, thus leading us to the middle (value of slow pointer) when fast pointer reaches the end.

*/

namespace Precourse2
{
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
    public class LinkedList
    {
        public Node head; // head of linked list 

        /* Linked list node */
        

        /* Function to print middle of linked list */
        //Complete this function
        void printMiddle()
        {
            //Write your code here
            //Implement using Fast and slow pointers

            Node slow = head;
            Node fast = head;

            while(fast!=null && fast.next!=null)
            {
                slow = slow.next;
                fast = fast.next.next;
            }
            Console.WriteLine("Middle node data : " + slow.data);
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
                Console.Write(tnode.data + "->");
                tnode = tnode.next;
            }
            Console.Write("NULL");
        }

        public static void Main(String[] args)
        {
            LinkedList llist = new LinkedList();
            for (int i = 15; i > 0; --i)
            {
                llist.push(i);
                llist.printList();
                llist.printMiddle();
            }
        }
    }
}
using System;
namespace Algorithms
{
    /// Time Complexity : O(sn)
    // Space Complexity :O(1)
    // Did this code successfully run on Leetcode : Tested on VS
    // Any problem you faced while coding this : No
    public class LinkedListMidPoint
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
        public void printMiddle()
        {
            //Write your code here
            //Implement using Fast and slow pointers
            //When the fast pointer reaches the end slow pointer will reach the middle of the linked list
            Node fast_pntr = head;
            Node slow_pntr = head;
            if(head != null)
            {
                while(fast_pntr != null && fast_pntr.next != null)
                {
                    fast_pntr = fast_pntr.next.next;
                    slow_pntr = slow_pntr.next;
                }
                Console.WriteLine("The middle element is [" +
                                          slow_pntr.data + "] \n");
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
                Console.WriteLine(tnode.data + "->");
                tnode = tnode.next;
            }
            Console.WriteLine("NULL");
        }


    }
}

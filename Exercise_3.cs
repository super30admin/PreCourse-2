//Time Complexity O(n) where n is no. of elements
//Space Complexity O(1)
using System;

public class Node
{
    public int data;
    public Node next;

    public Node(int value)
    {
        data = value;
        next = null;
    }
}

public class LinkedList
{
    public Node head;

    public void Add(int data)
    {
        Node newNode = new Node(data);
        if (head == null)
        {
            head = newNode;
        }
        else
        {
            Node current = head;
            while (current.next != null)
            {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    public Node FindMidPoint()
    {
        if (head == null)
        {
            return null; // return null if empty
        }

        Node slow = head;
        Node fast = head;

        // Move fast by two nodes and slow by one node in each step
        while (fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Slow is now at the middle node
        return slow;
    }

    public void PrintList()
    {
        Node current = head;
        while (current != null)
        {
            Console.Write(current.data + " ");
            current = current.next;
        }
        Console.WriteLine();
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        // Create a linked list
        LinkedList list = new LinkedList();

        for (int i = 15; i > 0; --i)
        {
            list.Add(i);
            list.PrintList();
            list.FindMidPoint();
        }

        
        Console.WriteLine("The linked list:");
        list.PrintList();

        // Find the middle node
        Node midNode = list.FindMidPoint();

        if (midNode != null)
        {
            Console.WriteLine("The middle element is: " + midNode.data);
        }
        else
        {
            Console.WriteLine("The list is empty.");
        }
    }
}

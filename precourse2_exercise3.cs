using System;

namespace precourse2_exercise3
{
    class precourse2_exercise3
    {
        static Node head;
        static int n=1;
        public class Node
        {
            public int data;
            public  Node next;
            public Node(int d)
            {
                data = d;
                next = null;
            }
        }

        public void printmiddle()
        {

            Node tnode = head.next;
            //n = 1;
            printmiddleutil(tnode);

        }

        public void printmiddleutil(Node no)
        {
            if(no==null)
            {
                n = (n) / 2;
                return;
            }

            n = n + 1;
            printmiddleutil(no.next);
            n = n - 1;
            if(n==0)
            {
                head = no;
                Console.WriteLine("midpoint node is {0}", head.data);
            }

        }

        public void Push(int newdata)
        {
            Node _newnode = new Node(newdata);
            _newnode.next = head;
            head = _newnode;
        }

        public void printlist()
        {
            Node tnode = head;
            while (tnode!=null)
            {
                Console.WriteLine("printlist {0}", tnode.data);
                tnode=tnode.next;
            }
        }

        static void Main(string[] args)
        {

            precourse2_exercise3 ll = new precourse2_exercise3();
            for (int i = 15; i > 0; --i)

            {
                ll.Push(i);
            }
                ll.printlist();
                ll.printmiddle();
            
                Console.WriteLine("Hello World!");
        }
    }
}

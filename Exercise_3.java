// Operation:        middle element
// Time Complexity:        n
// Space Complexity:       1
// Yes, this code ran successfully
// No, I didn't face any problem in this problem statement

class LinkedList {
    Node head; // head of linked list

    /* Linked list node */
    class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    /* Function to print middle of linked list */
    //Complete this function
    void printMiddle() {
        //Write your code here
        //Implement using Fast and slow pointers
        Node fast = head;                               // Pointer 1 : fast set to head
        Node slow = head;                               // Pointer 2 : slow set to head
        while (fast!= null && fast.next != null) {
            fast = fast.next.next;                      // fast pointer running with 2 increment
            slow = slow.next;                           // slow pointer running with 1 increment
        }
        System.out.println(slow.data);                  // slow pointer would be on its correct position
    }

    public void push(int new_data) {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }

    public void printList() {
        Node tnode = head;
        while (tnode != null) {
            System.out.print(tnode.data + "->");
            tnode = tnode.next;
        }
        System.out.println("NULL");
    }
}

public class Exercise_3
{
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
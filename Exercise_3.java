/*Time Complexity : O(n)
 Space Complexity : O(1), no additional cost

 Your code here along with comments explaining your approach:
 Keep two pointer slow and fast pointing at the head of the linked list.
 Fast pointer moves twice as much as slow pointer. Once the fast pointer
 reaches the end of the list, since slow pointer only travelled half of the
 fast pointer, the slow pointer now points to the middle value of list.
*/


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
        Node slow = head;
        if (slow == null) {
            /*If not elements in list*/
            System.out.println("List is empty");
            return;
        }

        Node fast = head.next;
        if (fast == null) {
            /*if ony 1 element in the list, we print that as mid element*/
            System.out.println(head.data);
            return;
        }
        while (fast.next != null) {
            fast = fast.next;
            if (fast.next != null) {
                fast = fast.next;
            }
            slow = slow.next;
        }
        System.out.println(slow.data);
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

    public static void main(String[] args) {
        LinkedList llist = new LinkedList();
        for (int i = 15; i > 0; --i) {
            llist.push(i);
            llist.printList();
            llist.printMiddle();
        }
    }
} 
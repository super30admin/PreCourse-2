//TC: O(n) where n is size of linkedlist
//SC: O(n) where n is size of linkedlist, to store the list, no additional space required

class LinkedList {
    Node head; // head of linked list 

    class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    //Complete this function
    void printMiddle() {
        //Write your code here
        //Implement using Fast and slow pointers
        Node top = head;
        Node mid = head;
        while (top != null && top.next != null) {
            top = top.next.next;
            mid = mid.next;
        }
        System.out.println("Middle node of linkedlist is : " + mid.data);
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

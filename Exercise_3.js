//Time Complexity O(n)
//Space Complexity O(1)
//Yes
//No

class LinkedList {
    constructor() {
        this.head = null; // head of linked list
    }

    /* Linked list node */
    static Node = class {
        constructor(d) {
            this.data = d;
            this.next = null;
        }
    }

    /* Function to print middle of linked list */
    printMiddle() {
        // Implement using Fast and Slow pointers
        let slow = this.head; //Intialize fats and slow pointers to head
        let fast = this.head;

        while (fast != null && fast.next != null) {
            slow = slow.next; // Move slow pointer one step
            fast = fast.next.next; // Move fast pointer two steps
        }

        console.log("Middle element: " + slow.data);
    }

    push(new_data) {
        // Insert a new node at the beginning of the linked list
        let new_node = new LinkedList.Node(new_data);
        new_node.next = this.head;
        this.head = new_node;
    }

    printList() {
        let tnode = this.head;
        while (tnode != null) {
            console.log(tnode.data + "->");
            tnode = tnode.next;
        }
        console.log("NULL");
    }
}

let llist = new LinkedList();
for (let i = 15; i > 0; --i) {
    llist.push(i);
    llist.printList();
    llist.printMiddle();
}

class LinkedList {
    constructor() {
        this.head = null; // head of linked list
    }

    /* Linked list node */
    static Node = class {
        constructor(d) {
            this.data = d; // Store data
            this.next = null; // Pointer to next node
        }
    }

    // Function to print the middle of the linked list
    printMiddle() {
        let slow = this.head;
        let fast = this.head;

        // Traverse the list with fast and slow pointers
        while (fast != null && fast.next != null) {
            slow = slow.next; // slow pointer moves one step
            fast = fast.next.next; // fast pointer moves two steps
        }

        // When fast pointer reaches the end, slow pointer will be at the middle
        if (slow != null) {
            console.log("Middle element is " + slow.data);
        }
    }

    // Function to push a new node to the front of the list
    push(new_data) {
        let new_node = new LinkedList.Node(new_data); // Correctly reference LinkedList.Node
        new_node.next = this.head;
        this.head = new_node;
    }

    // Function to print the linked list
    printList() {
        let tnode = this.head;
        while (tnode != null) {
            console.log(tnode.data + " -> ");
            tnode = tnode.next;
        }
        console.log("NULL");
    }
}

// Driver code
let llist = new LinkedList();
for (let i = 15; i > 0; --i) {
    llist.push(i);  // Insert nodes to the list
    llist.printList();  // Print the list
    llist.printMiddle();  // Print the middle element
}

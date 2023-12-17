class LinkedList {
    constructor() {
        this.head = null; // head of linked list
    }
    /* Linked list node */
    static Node = class {
       constructor(d) {
       //Constructor here
       this.data = d;
       this.next = null;
       }
    }
    /* Function to print middle of linked list */
    //Complete this function
     printMiddle() {
        //Write your code here
       	//Implement using Fast and slow pointers
        let length = 0;
        let temp = this.head;

        // Calculate the length of the linked list
        while (temp !== null) {
            length++;
            temp = temp.next;
        }
        // Traverse to the middle element
        temp = this.head;
        for (let i = 0; i < Math.floor(length / 2); i++) {
            temp = temp.next;
        }

        console.log("Middle element: " + temp.data);

    }
     push(new_data) {
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

 

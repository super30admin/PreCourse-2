class LinkedList {
    constructor() {
        this.head = null; // head of linked list
    }
​
    /* Linked list node */
    static Node = class {
       constructor(d) {
       //Constructor here
       this.data = d;
       this.next = null;
       }
    }
​
    /* Function to print middle of linked list */
    //Complete this function
    function printMiddle() {
        //Write your code here
       	//Implement using Fast and slow pointers
    }
​
    function push(new_data) {
        let new_node = new this.Node(new_data);
        new_node.next = this.head;
        this.head = new_node;
    }
​
    function printList() {
        let tnode = this.head;
        while (tnode != null) {
            console.log(tnode.data + "->");
            tnode = tnode.next;
        }
        console.log("NULL");
    }
}
​
let llist = new LinkedList();
for (let i = 15; i > 0; --i) {
    llist.push(i);
    llist.printList();
    llist.printMiddle();
}

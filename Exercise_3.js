// Time Complexity : O(N)
// Space Complexity : O(1)
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
    printMiddle() {
        //Write your code here
       	//Implement using Fast and slow pointers
           let slow = this.head;
           let fast = this.head;
   
           if (this.head != null) {
               // Move fast by 2 and slow by 1
               while (fast != null && fast.next != null) {
                   fast = fast.next.next;
                   slow = slow.next;
               }
               console.log("Middle element is: " + slow.data);
           }
    }
​
    push(new_data) {
        let new_node = new this.Node(new_data);
        new_node.next = this.head;
        this.head = new_node;
    }
​
    printList() {
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

/*
* TC: push O(1) print O(n)
* SC: O(n)
* */

/* Linked list node */
class Node {
  constructor(d) {
    //Constructor here
    this.data = d;
    this.next = null;
  }
};


class LinkedList {
  constructor() {
    this.head = null; // head of linked list
  }

  /* Function to print middle of linked list */

  //Complete this function

  printMiddle() {
    //Write your code here
    //Implement using Fast and slow pointers
      let slow = this.head;
      let fast = this.head

      while (fast !==null && fast.next !== null ) {
          slow = slow.next;
          fast = fast.next.next;
      }
      return slow.data
  }

  push(new_data) {
    let new_node = new Node(new_data);
    new_node.next = this.head;
    this.head = new_node;
  }

  printList() {
    let tnode = this.head;
    while (tnode != null) {
      console.log(tnode.data + '->');
      tnode = tnode.next;
    }
    console.log('NULL');
  }
}

let llist = new LinkedList();
for (let i = 15; i > 0; --i) {
  llist.push(i);
  llist.printList()
  llist.printMiddle();
}

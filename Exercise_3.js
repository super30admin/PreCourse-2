//Time Complexity: O(n)
//Space Complexity: O(1)

// Node class

class Node {
  constructor(data = null, next = null) {
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(new_data) {
    let newNode = new Node(new_data);
    if (!this.head) {
      this.head = newNode;
      this.tail = this.head;
    } else {
      this.tail.next = newNode;
      this.tail = this.tail.next;
    }
    this.length += 1;
    return this;
  }
  // Function to get the middle of the linked list
  printMiddle() {
    let counter = 0;
    let cur_node = this.head;
    let mid_node = this.head;
    while (cur_node != null) {
      if (counter % 2 === 1) {
        mid_node = mid_node.next;
      }
      counter += 1;
      cur_node = cur_node.next;
    }
    return mid_node.data;
  }
}
//  Driver code
let list1 = new LinkedList();
list1.push(5);
list1.push(4);
list1.push(2);
list1.push(3);
list1.push(1);
console.log(list1.printMiddle());

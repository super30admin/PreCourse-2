// Time Complexity: O(n)
// Space Complexity: O(1)
// Did this code successfully run on Leetcode: N/A
// Any problem you faced while coding this: No.

class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  append(value) {
    const newNode = new Node(value);
    let currentNode;
    if (!this.head) {
      this.head = newNode;
      this.size++;
    } else {
      currentNode = this.head;
      while (currentNode.next) {
        currentNode = currentNode.next;
      }
      currentNode.next = newNode;
      this.size++;
    }
  }

  findMidPoint() {
    if (this.size === 0) {
      return console.log(
        "midPoint value can not be found because list is empty"
      );
    }

    if (this.size < 3) {
      return console.log("this is midPoint value:", this.head.data);
    }

    let iterator = 0;
    let currentNode = this.head;
    let midPoint = Math.floor(this.size / 2);

    while (currentNode.next) {
      if (iterator === midPoint) {
        return console.log("this is midPoint value:", currentNode.data);
      }
      currentNode = currentNode.next;
      iterator++;
    }
  }
}

const currentList = new LinkedList();
// appends to list
currentList.append(5);
currentList.append(4);
currentList.append(3);
currentList.append(2);
currentList.append(1);

// Finds mid point of LinkedList and returns 3
currentList.findMidPoint();

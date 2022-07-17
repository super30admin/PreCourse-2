class Node {
    constructor(data, nextNode = null) {
      this.data = data;
      this.nextNode = nextNode;
    }
  }
  
  class LinkedList {
    constructor(head = null) {
      this.head = head;
    }
  
    push(data) {
      let newNode = new Node(data);
      if (this.head == null) {
        this.linkedList = new LinkedList(newNode);
  
      } else {
        newNode.next = this.head;
      }
      this.head = newNode;
    }
  
    printMiddle() {
      var middle = this.head;
      var tempHead = this.head;
      var count = 0;
      while (tempHead != null) {
        if ((count % 2) === 1)
          middle = middle.next;
  
        ++count;
        tempHead = tempHead.next;
      }
  
      // If empty list is provided
      if (middle != null)
        console.log(middle.data);
    }
  
    printList() {
      let tempNode = this.head;
      while (tempNode.next) {
        console.log(tempNode.data);
        tempNode = tempNode.next;
      }
    }
  }
  
  let linkedList = new LinkedList();
  for (let i = 3; i > 0; --i) {
    linkedList.push(i);
    linkedList.printList();
    linkedList.printMiddle();
  }
  
  
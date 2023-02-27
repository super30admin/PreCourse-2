// Find Mid Point of a Singly Linked List.
class Node {
  constructor(value, next=null) {
    this.value = value
    this.next = next
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null
    this.tail = null
    this.size = 0
  }

  append(value) {
    const node = new Node(value)

    if (!this.head) {
      this.head = node
      this.tail = node
    } else {
      this.tail.next = node
      this.tail = node
    }

    this.size++
  }

  printMiddle() {
    let slow = this.head
    let fast = this.head
    
    while(fast && fast.next) {
      slow = slow.next
      fast = fast.next.next
    }

    return slow
  }
}

// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
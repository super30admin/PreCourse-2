// Time Complexity :
// Space Complexity :
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach
// Exercise_3 : Find Mid Point of a Singly Linked List.

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val);
    this.next = (next === undefined ? null : next);
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function (head) {
    // Keep 2 pointers: falst and slow. 
    // Fast moves twice the speed of slow.
    // When fast reaches end, slow will be at mid point
    let fast = slow = head;
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }
}

let head = new ListNode(1); 
head.next = new ListNode(2); 
head.next.next = new ListNode(3); 
head.next.next.next = new ListNode(4); 
head.next.next.next.next = new ListNode(5); 
console.log(middleNode(head));
// Exercise_3 : Find Mid Point of a Singly Linked List.

var middleNode = function(head) {
    let slow = head;
    let fast = head;
    while(fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
};            
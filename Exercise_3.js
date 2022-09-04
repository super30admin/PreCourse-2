class LinkedList {
    constructor(data, head){
        this.data = data
        this.next = null;
        this.head = head;
    }
    push(head, element){
        var node = new LinkedList(head, element);
        var current;
        if (this.head == null)
            this.head = node;
        else {
            current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = node;
        }
    }
    middleNode(head) {
        let fast = head.next
        while(fast){
            head = head.next
            fast = fast.next.next
        }
        console.log(head.data);
        return head
    };
}
list1 = new LinkedList() 
list1.push(list1,5)
list1.push(list1, 4) 
list1.push(list1, 2) 
list1.push(list1, 3) 
list1.push(list1, 1) 
list1.middleNode(list1) 
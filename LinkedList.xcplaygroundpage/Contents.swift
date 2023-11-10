// Time complexity O(n)
// Space complexity O(1)

class Node {
    var data: Int
    var next: Node?
    
    init(_ value: Int) {
        self.data = value
    }
}

class LinkedList {
    var head: Node?
    var tail: Node?
    
    init(_ node: Node) {
        head = node
        tail = nil
    }
    
    func insert(_ node: Node)  {
        node.next = self.head
        self.head = node
    }
    
    func printNodes()  {
        var node = head
        
        while node != nil {
            print(node!.data)
            node = node!.next
        }
        
    }
    
    func lengthOfList() -> Int {
        var count = 0
        var node = head
        
        while node != nil {
            count += 1
            print(node!.data)
            node = node!.next
        }
        return count
    }
    
    func middle() -> Node? {
        let middle  = self.lengthOfList() / 2
        var node: Node? = head
        for _ in  0..<middle {
            node = node?.next
        }
        return node
    }
    
    func findMiddleFast() -> Node? {
        var slowPointer = head, fastPointer = head
        while fastPointer != nil && fastPointer?.next != nil {
            slowPointer = slowPointer?.next
            fastPointer = fastPointer?.next?.next
        }
        return slowPointer
    }

}

let linkedList = LinkedList.init(Node.init(5))
linkedList.insert(Node.init(10))
//linkedList.insert(Node.init(15))
//linkedList.insert(Node.init(20))
//linkedList.insert(Node.init(25))
linkedList.lengthOfList()
let middle = linkedList.findMiddleFast()
middle?.data

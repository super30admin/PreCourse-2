import Foundation

// Time Complexity | size = O(n) | push =  O(1) | middleElement = O(n) | middleElementMethod2 = O(n)
// Space Complexity | size = O(1) | push = O(n) | middleElement = O(1) | middleElementMethod2 = O(1)
class Node<T> {
    let value: T
    var next: Node<T>?
    
    init(value: T, next: Node<T>? = nil) {
        self.value = value
        self.next = next
    }
}

class LinkedList<T> {
    var head: Node<T>?
    
    var isEmpty: Bool {
        return head == nil
    }
    
    func size() -> Int {
        var temp = head
        var count = 0
        
        while temp != nil {
            temp = temp?.next
            count += 1
        }
        return count
    }
    
    func push(newValue: T) {
        let newNode = Node(value: newValue)
        
        newNode.next = head
        head = newNode
    }
    
    
    func middleElement() -> T? {
        var temp = head
        var middleElementIndex = self.size()/2
        while middleElementIndex > 0 {
            temp = temp?.next
            middleElementIndex -= 1
        }
        return temp?.value
    }
    
    
    func middleElementMethod2() -> T? {
        var fastPtr = head
        var slowPtr = head
        
        while( fastPtr != nil && fastPtr?.next != nil) {
            fastPtr = fastPtr?.next?.next
            slowPtr = slowPtr?.next
        }
        return slowPtr?.value
    }
}


extension Node: CustomStringConvertible {
    var description: String {
        guard let next = next else {
            return "\(value)"
        }
        return "\(value) -> " + String(describing: next) + " "
    }
}

extension LinkedList: CustomStringConvertible {
    var description: String {
        guard let head = head else {
            return "Empty List"
        }
        return String(describing: head)
    }
}


var linkedList = LinkedList<Int>()
linkedList.push(newValue: 1)
linkedList.push(newValue: 2)
linkedList.push(newValue: 3)
linkedList.push(newValue: 4)
linkedList.push(newValue: 5)

print(linkedList)

print(linkedList.size())

print(linkedList.middleElement()!)

print(linkedList.middleElementMethod2()!)

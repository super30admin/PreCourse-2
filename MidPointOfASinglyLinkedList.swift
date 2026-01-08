//
//  MidPointOfASinglyLinkedList.swift
//  DSA-Practice
//
//  Created by Paridhi Malviya on 12/22/25.
//

class MidPointOfASinglyLinkedList {
    
    init() {
        let linkedList = SinglyLinkedList<Int>()
        linkedList.append(value: 1)
        linkedList.append(value: 4)
        linkedList.append(value: 2)
        linkedList.append(value: 6)
        linkedList.append(value: 10)
        
        findLLMidPoint(linkedList: linkedList)
    }
    
    func findLLMidPoint(linkedList: SinglyLinkedList<Int>) {
        
        var slow = linkedList.currentHead()
        var fast = linkedList.currentHead()
        while (fast?.next != nil && fast?.next?.next != nil) {
            slow = slow?.next
            fast = fast?.next?.next
        }
        print("mid point of the linked list is \(slow?.value, default: "NA")")
    }
    
}

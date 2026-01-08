//
//  InerativeQuickSort.swift
//  DSA-Practice
//
//  Created by Paridhi Malviya on 12/22/25.
//

class IterativeQuickSort {
    
    init() {
        var array = [8, 5, 1, 13, 7, 12, 9, 6]
        iterativeQuickSort(array: &array, low: 0, high: array.count - 1)
        print("sorted array using iterative quick sort \(array)")
    }
    
    func iterativeQuickSort(array: inout [Int], low: Int, high: Int) {
        guard array.count > 1 else {
            return
        }
        
        //Stack stores (low, high) index pairs
        let stack = StackUsingLL<(Int, Int)>(llList: LLLinkedList())
        stack.push(value: (low, high))
        
        while let (low, high) = stack.pop() {
            //we got low and high index
            //do partition in here. We will get pivot index. then push in stack the tuple of (low, high) indices which needs to be sorted. It's the same as the recursive approach, it's just that we are creating stack of our own instead of using system's call stack
            if (low >= high) {
                return
            }
            let pivotIndex = partitionTheArrayBasedOnAPivot(array: &array, low: low, high: high, pivot: array[high])
            
            //push left side
            if (low < pivotIndex - 1) {
                stack.push(value: (low, pivotIndex - 1))
            }
            
            //push right side
            if (pivotIndex + 1 < high) {
                stack.push(value: (pivotIndex + 1, high))
            }
        }
    }
    
    func partitionTheArrayBasedOnAPivot(array: inout [Int], low: Int, high: Int, pivot: Int) -> Int {
        
        /*
         it makes use of 2 pointers.
         0-(j-1) pointer indicates the node which are smaller than or equal to the pivot
         j - (i-1) indicates the elements larger than the pivot
         i to end -> indicates the unvisited items
         */
        
        var j = low
        var i = low
        while (i <= high) {
            if (array[i] <= pivot) {
                if i != j { array.swapAt(i, j) }
                i += 1
                j += 1
            } else {
                i += 1
            }
        }
        //return the pivot index from here
        return j - 1
    }
}

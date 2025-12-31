//
//  MergeSort.swift
//  DSA-Practice
//
//  Created by Paridhi Malviya on 12/22/25.
//

class MergeSort {
    
    init() {
        let a = [1, 2, 14, 23, 5, 80, 10]
        let result = sortUsingMergeSort(inputArray: a, low: 0, high: a.count - 1)
        print("result is \(result) using merge sort")
    }
    
    func sortUsingMergeSort(inputArray: [Int], low: Int, high: Int) -> [Int] {
        //base case - if only 1 element is left
        if (low == high) {
            return [inputArray[low]]
        }
        
        let mid = (low + high) / 2
        let firstSortedArray = sortUsingMergeSort(inputArray: inputArray, low: low, high: mid)
        let secondSortedArray = sortUsingMergeSort(inputArray: inputArray, low: mid + 1, high: high)
        
        let sortedArray = mergeTwoSortedArray(a: firstSortedArray, b: secondSortedArray)
        return sortedArray
    }
    
    func mergeTwoSortedArray(a: [Int], b: [Int]) -> [Int] {
        var resultArray = [Int]()
        
        var i = 0
        var j = 0
        
        while (i < a.count && j < b.count) {
            if (a[i] < b[j]) {
                resultArray.append(a[i])
                i += 1
            } else {
                resultArray.append(b[j])
                j += 1
            }
        }
        
        while(i < a.count) {
            resultArray.append(a[i])
            i += 1
        }
        while(j < b.count) {
            resultArray.append(b[j])
            j += 1
        }
        
        return resultArray
    }
    
    func mergeTwoSortedArrays(a: [Int], b: [Int]) -> [Int] {
        var resultArray = Array(repeating: 0, count: a.count + b.count)
        var i = 0
        var j = 0
        var k = 0
        print("resultARray \(resultArray)")
        while (i < a.count && j < b.count) {
            if a[i] < b[j] {
                resultArray[k] = a[i]
                i += 1
                k += 1
            } else {
                resultArray[k] = b[j]
                j += 1
                k += 1
            }
        }
        
        while (i < a.count) {
            resultArray[k] = a[i]
            i += 1
            k += 1
        }
        
        while (j < b.count) {
            resultArray[k] = b[j]
            j += 1
            k += 1
        }
        return resultArray
    }
}



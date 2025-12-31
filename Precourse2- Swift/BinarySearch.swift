//
//  Untitled.swift
//  DSA-Practice
//
//  Created by Paridhi Malviya on 12/17/25.
//

/*
 prerequisites -  the array must be sorted.
 2 approaches - iterative bonary search algorithm, recursive binary search algorithm
 complexity to search for an element - O(log n)
*/

class BinarySearch {
    
    init() {
        let sortedArray = [2, 5, 8, 12, 16, 23, 38, 56, 71, 91]
        let targetValue = 23
        if let index = binarySearch(for: targetValue, in: sortedArray) {
            print("element \(targetValue) found at index \(index)")
        } else {
            print("Element \(targetValue) not found in the array")
        }
    }

    func binarySearch(for target: Int, in array: [Int]) -> Int? {
        var left = 0
        var right = array.count - 1
        while left <= right {
            let middle = (left + right) / 2
            let value = array[middle]
            if value == target {
                return middle //target found, return it's index
            } else if value < target {
                left = middle + 1 //target is in the right half
            } else {
                right = middle - 1 //target is in the left half
            }
        }
        return -1 //Target not found
    }
    
    func recursiveBinarySearch(for target: Int, in array: [Int], left: Int = 0, right: Int?) -> Int? {
        
        let right = right ?? array.count - 1
        
        guard left < right else {
            return nil
        }
        
        let middle = (left + right) / 2
        let value = array[middle]
        if target == value {
            return middle
        } else if value < target {
            return recursiveBinarySearch(for: target, in: array, left: middle + 1, right: right)
        } else {
            return recursiveBinarySearch(for: target, in: array, left: left, right: middle - 1)
        }
    }
}

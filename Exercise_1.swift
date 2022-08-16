import Cocoa


// Time Complexity - Best = O(1) | Worst = O(logn)
// Space Complexity - O(logn)

func binarySearch(arr: [Int], startIndex: Int, endIndex: Int, searchElement: Int) -> Int {
if startIndex > endIndex {
    return -1
}
    let middleElementIndex = (startIndex + endIndex)/2
    let middleElement = arr[middleElementIndex]
    var resultIndex = 0
    if middleElement == searchElement {
        resultIndex =  middleElementIndex
    } else if middleElement > searchElement {
       return binarySearch(arr: arr, startIndex: 0, endIndex: middleElementIndex - 1, searchElement: searchElement)
    } else if middleElement < searchElement{
        return binarySearch(arr: arr, startIndex: middleElementIndex + 1, endIndex: endIndex, searchElement: searchElement)
    }
    return resultIndex
}
let arr = [100, 200, 300, 310, 511, 600]

print(binarySearch(arr: arr, startIndex: 0, endIndex: arr.count - 1, searchElement: 300))

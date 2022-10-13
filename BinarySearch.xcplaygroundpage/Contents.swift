// Binary search array.

func binarySearch(_ array:[Int], _ start: Int, _ end: Int, _ target: Int) -> Int {
    if end < start {
        return -1
    }
    let middle = start + (end - start) / 2
    print("Middle is \(middle)")
    let value = array[middle]
    print("Value is \(value)")
    if value == target {
        return middle
    } else {
       return target > value ? binarySearch(array, middle + 1, end, target) : binarySearch(array, start, middle - 1, target)
    }
}

//func binarySearch(_ array:[Int], _ start: Int, _ end: Int, _ target: Int) -> Int {
//    var loopStart = start, loopEnd = end
//    var result = -1
//    while loopStart < loopEnd {
//        let middle = start + (end - start) / 2
//        print("Middle is\(middle)")
//        print("Value is \(array[middle])")
//        if array[middle] == target {
//            result = middle
//            break
//        } else if array[middle] > target {
//            loopEnd = middle - 1
//        } else {
//            loopStart = middle +  1
//        }
//        
//    }
//    return result
//}

let myArray = [-1,0,3,5,9,12]

 binarySearch(myArray, 0 , myArray.count - 1, 0)

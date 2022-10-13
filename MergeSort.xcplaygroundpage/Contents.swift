// Time complexity O(nLogN)

func mergeSort(_ array: inout [Int],_ low: Int,_ high: Int)  {
    if low < high {
        let middle = low + (high - low) / 2
        mergeSort(&array, low, middle)
        mergeSort(&array, middle + 1, high)
        merge(&array, low, middle, high)
    }
}

func merge(_ array: inout [Int],_ low: Int,_ middle: Int,_ high: Int) {
    let n1 = middle - low + 1
    let n2 = high - middle
    
    var lArray = [Int](repeating: 0, count: n1)
    var rArray = [Int](repeating: 0, count: n1)
    
    for index in 0..<n1 {
        lArray[index] = array[low + index]
    }
    for index in 0..<n2 {
        rArray[index] = array[middle + 1 + index]
    }
    
    var i = 0, j = 0
    var k = low
    
    while i < n1 && j < n2 {
        if lArray[i] <= rArray[j] {
            array[k] = lArray[i]
            i += 1
        } else {
            array[k] = rArray[j]
            j += 1
        }
        k += 1
    }
    
    while i < n1 {
        array[k] = lArray[i]
        i += 1
        k += 1
    }
    
    while j < n2 {
        array[k] = rArray[j]
        j += 1
        k += 1
    }
}

var array =  [50, 40, 30, 20, 10]

mergeSort(&array, 0, array.count - 1)
